import pandas as pd
import statistics as s
import matplotlib.pyplot as plt
# actual drift point: 540

#actual drift point gradual: 540

# if the first lie of each group is >= 540 and DriftType.Sudden ==> TP else ==> FP

# missed wäre wenn wir keinen drift detected haben also die Group keine Einträhehat ==> len(group) == 0

# drifts davor 540 und nach dem ersten drift sind FP (Overestimations)

# incorporate only the true positives
def calc_latency():
    file_path = 'ExperimentsDocker/gradual_100.csv'
    df = pd.read_csv(file_path)
    tuple_list = []
    #filter out the true postives and save (MS and event)
    for (experiment, trace_threshold, anomaly_threshold), group in df.groupby(['Experiment','Trace Threshold', 'Anomaly Threshold']):
        counter = 0
        for index, row in group.iterrows():
                if row["Drifts detected"] == "DriftType.SUDDEN" and row["at event"] >= 540 and counter == 0:
                    tuple_list.append((row["Anomaly Threshold"], row["at event"]))
                    break
                
                counter += 1
    print(tuple_list)
    return tuple_list
    #print(tuple_list)

#list = calc_latency()

def corr_from_tuple_list(tuple_list):

    df = pd.DataFrame(tuple_list, columns=['MS', 'event'])
    df['event'] = df['event'] - 540
    corr = df["MS"].corr(df["event"])
    print(corr)
    plt.scatter(df["MS"], df["event"], color='purple')

    # Adding title and labels
    #plt.title('')
    plt.xlabel('Model Score')
    plt.ylabel('Latency Lag')

    # Show the plot
    plt.show()

#corr_from_tuple_list(list)

def calc_accuracy():
    file_path = 'ExperimentsDocker/gradual_100.csv'
    df = pd.read_csv(file_path)
    confusion_matrices = {}

    for (experiment, trace_threshold, anomaly_threshold), group in df.groupby(['Experiment','Trace Threshold', 'Anomaly Threshold']):
        FN = 0
        TP = 0
        FP = 0
        lenght_group = len(group)
        if lenght_group == 0:
            FN = 1
            TP = 0
            FP = 0
        else:

            for index, row in group.iterrows():
                if row["Drifts detected"] == "DriftType.SUDDEN" and row["at event"] >= 540 and TP == 0:
                    TP = 1
                else:
                    FP += 1
                
        
        confusion_matrices[(experiment, trace_threshold, anomaly_threshold)] = {'TP': TP, 'FP': FP, 'FN': FN}

    #aggregate data througout the 10 experiments
    aggregated_data = {}

    for key, value in confusion_matrices.items():
        trace, anomaly = key[1], key[2]
        ttuple= (trace, anomaly)  
        if ttuple not in aggregated_data:
            aggregated_data[ttuple] = {'TP': 0, 'FP': 0, 'FN': 0}
        aggregated_data[ttuple]['TP'] += value['TP']
        aggregated_data[ttuple]['FP'] += value['FP']
        aggregated_data[ttuple]['FN'] += value['FN']

    return aggregated_data
    

#dict = calc_accuracy()
#print(dict)
#print(len(dict))

def to_matrix(numbers_dict):
    accuracy_dict = {}

    for key, values in numbers_dict.items():
        if (values['TP'] + values['FN']) > 0:  
            accuracy = values['TP'] / (values['TP'] + values['FP'] + values['FN'])
        else:
            accuracy = 0 
        accuracy_dict[key] = accuracy
    print(accuracy_dict)
          
#to_matrix(dict)     

def calc_average_detection_delay(weglassen: bool):

    actual_point = 540
    file_path = 'ExperimentsDocker/sudden_100.csv'
    df = pd.read_csv(file_path)
    delays = []


    for (trace_threshold, anomaly_threshold), group in df.groupby(['Trace Threshold', 'Lower Boundary']):
        if weglassen and trace_threshold == 0.8 and anomaly_threshold == 0.5:
               continue
        first_row = group.iloc[0]
        delays.append(first_row['at event'])
    
    differences = [abs(actual_point - delay) for delay in delays]
    average_delay = sum(differences) / len(differences)
    return average_delay

#average_detection_delay = calc_average_detection_delay(weglassen=True)
#print("Average Detection Delay:", average_detection_delay)

def find_largest_group():

    file_path = 'ExperimentsDocker/sudden_100.csv'
    df = pd.read_csv(file_path)
    
    group_sizes = df.groupby(['Trace Threshold', 'Lower Boundary']).size()
    
    # Find the group with the maximum size
    max_size = group_sizes.max()
    largest_group = group_sizes[group_sizes == max_size]
    
    # Get the indices of the largest group
    largest_combination = largest_group.index.values[0]
    
    return largest_combination, max_size

#combi, size = find_largest_group()

#print(combi)
#print(size)
def average_execution_time(weglassen: bool):
     file_path = 'ExperimentsDocker/sudden_100.csv'
     df = pd.read_csv(file_path)
     exe_times = []
     for (trace_threshold, anomaly_threshold), group in df.groupby(['Trace Threshold', 'Lower Boundary']):
        if weglassen and trace_threshold == 0.8 and anomaly_threshold == 0.5:
               continue
        first_row = group.iloc[0]
        exe_times.append(first_row['exe time'])


     avg = s.mean(exe_times)
     std = s.stdev(exe_times)
     print(avg)
     print(std)

#average_execution_time(weglassen=True)
     


        

