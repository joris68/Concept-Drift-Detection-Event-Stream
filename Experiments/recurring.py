import pandas as pd
import statistics as s

# first Point 341

# second point 697


def calc_accuracy():
     file_path = 'ExperimentsDocker/recurring_100.csv'
     df = pd.read_csv(file_path)
     confusion_matrices = {}

     # every rigth drift would depend on the 

     for (experiment, trace_threshold, anomaly_threshold), group in df.groupby([ "Experiment",'Trace Threshold', 'Anomaly Threshold']):

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
                    TP += 1
                elif row["Drifts detected"] == "DriftType.SUDDEN_RECURRING" and row["at event"] >= 697 and TP == 1: 
                    TP +=1
                else:
                    FP += 1
                
        confusion_matrices[(experiment, trace_threshold, anomaly_threshold)] = {'TP': TP, 'FP': FP, 'FN': FN}

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



dict = calc_accuracy()


def to_matrix(numbers_dict):
    accuracy_dict = {}

    for key, values in numbers_dict.items():
        if (values['TP'] + values['FN']) > 0:  
            accuracy = values['TP'] / (values['TP'] + values['FP'] + values['FN'])
        else:
            accuracy = 0 
        accuracy_dict[key] = accuracy
    print(accuracy_dict)

to_matrix(dict)


def calc_average_detection_delay(weglassen : bool):

    actual_point_first = 341
    actual_point_second = 697
    file_path = 'ExperimentsDocker/recurring_100.csv'
    df = pd.read_csv(file_path)
    delays_first = []
    delays_second = []


    for (trace_threshold, anomaly_threshold), group in df.groupby(['Trace Threshold', 'Lower Boundary']):
        if weglassen and trace_threshold == 0.8 and anomaly_threshold == 0.5:
               continue
        first_row = group.iloc[0]
        second_row = group.iloc[1]
        delays_first.append(first_row['at event'])
        delays_second.append(second_row['at event'])

    
    differences_first = [abs(actual_point_first - delay) for delay in delays_first]
    differences_second = [abs(actual_point_second - delay) for delay in delays_second]
    average_delay = (sum(differences_first) + sum(differences_second)) / (len(differences_first) + len(differences_second))
    print(average_delay)
    return average_delay


#calc_average_detection_delay(weglassen=True)

def find_largest_group():

    file_path = 'ExperimentsDocker/recurring_100.csv'
    df = pd.read_csv(file_path)
    
    group_sizes = df.groupby(['Trace Threshold', 'Lower Boundary']).size()
    
    # Find the group with the maximum size
    max_size = group_sizes.max()
    largest_group = group_sizes[group_sizes == max_size]
    
    # Get the indices of the largest group
    largest_combination = largest_group.index.values[0]
    
    return largest_combination, max_size

#combi, size = find_largest_group()

##print(combi)
#print(size)

def average_execution_time(weglassen: bool):
     file_path = 'ExperimentsDocker/recurring_100.csv'
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

        
