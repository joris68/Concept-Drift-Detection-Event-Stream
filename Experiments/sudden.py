import pandas as pd
import statistics as s
# actual drift point: 540

def calc_accracy(weglassen: bool):
    file_path = 'ExperimentsDocker/sudden_100.csv'
    df = pd.read_csv(file_path)
    confusion_matrices = {}

    for (trace_threshold, anomaly_threshold), group in df.groupby(['Trace Threshold', 'Lower Boundary']):
        if weglassen and trace_threshold == 0.8 and anomaly_threshold == 0.5:
               continue
        tp = group['Drifts detected'].eq('DriftType.SUDDEN').sum()
        # FN is calculated based on the provided criteria. If there's more than one row, it indicates potential FNs due to multiple entries or non-SUDDEN types.
        fn = len(group) - tp
        
        confusion_matrices[(trace_threshold, anomaly_threshold)] = {'TP': tp, 'FN': fn}


    total_tp = sum(cm['TP'] for cm in confusion_matrices.values())
    total_fn = sum(cm['FN'] for cm in confusion_matrices.values())

    print(total_tp)
    print(total_fn)

    accuracy = total_tp / (total_tp + total_fn)
    print(accuracy)

#calc_accracy(weglassen=True)

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

average_detection_delay = calc_average_detection_delay(weglassen=True)
print("Average Detection Delay:", average_detection_delay)

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
     


        

