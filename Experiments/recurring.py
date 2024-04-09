import pandas as pd
import statistics as s

# first Point 341

# second point 697


def calc_accuracy(weglassen: bool):
     file_path = 'ExperimentsDocker/recurring_100.csv'
     df = pd.read_csv(file_path)
     confusion_matrices = {}

     # every rigth drift would depend on the 

     for (trace_threshold, anomaly_threshold), group in df.groupby(['Trace Threshold', 'Lower Boundary']):

          if weglassen and trace_threshold == 0.8 and anomaly_threshold == 0.5:
               continue

    
          sorted_group = group.sort_values(by='Drifts detected')
          tp = 0
          fn = 0
     # Check first condition
          if sorted_group.iloc[0]['Drifts detected'] == 'DriftType.SUDDEN':
               tp += 1
          else:
               fn += 1
     
     # Check second condition if there's a second row
          if len(sorted_group) > 1 and sorted_group.iloc[1]['Drifts detected'] == 'DriftType.SUDDEN_RECURRING':
               tp += 1
          elif len(sorted_group) > 1:
               fn += 1

          # in the case the first got not 
          # Count remaining rows as FN
          fn += len(sorted_group) - 2
     
          confusion_matrices[(trace_threshold, anomaly_threshold)] = {'TP': tp, 'FN': fn}


     total_tp = sum(cm['TP'] for cm in confusion_matrices.values())
     total_fn = sum(cm['FN'] for cm in confusion_matrices.values())

     print(total_tp)
     print(total_fn)

     accuracy = total_tp / (total_tp + total_fn)
     print(accuracy)

#calc_accuracy(weglassen=True)


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
average_execution_time(weglassen=True)

        
