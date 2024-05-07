import pandas as pd
import statistics as s


# actual drift point: 540

def count_drifts(weglassen: bool):
     file_path = 'ExperimentsDocker/gradual_100.csv'
     df = pd.read_csv(file_path)
     incremental = 0
     sudden = 0
    #for (trace_threshold, anomaly_threshold), group in df.groupby(['Trace Threshold', 'Lower Boundary']):
      #  if weglassen and trace_threshold == 0.8 and anomaly_threshold == 0.5:
        #       continue

     grouped_df = df.groupby(['Trace Threshold', 'Lower Boundary']).first().reset_index()

     print(grouped_df[['Trace Threshold', 'Lower Boundary', 'Drifts detected']])

     average_at_event = grouped_df['at event'].mean()
     print(average_at_event)

     # Counting the types of Drifts detected in the first rows of each group
     drift_counts = grouped_df['Drifts detected'].value_counts()

     print(drift_counts)

#count_drifts(True)

def calc_accracy(weglassen: bool):
    file_path = 'New/gradual_100.csv'
    df = pd.read_csv(file_path)
    confusion_matrices = {}

    for (experiment, trace_threshold, anomaly_threshold), group in df.groupby(['Experiment','Trace Threshold', 'Anomaly Threshold']):
        if weglassen and trace_threshold == 0.8 and anomaly_threshold == 0.5:
               continue
        tp = group['Drifts detected'].eq('DriftType.SUDDEN').sum()
        # FN is calculated based on the provided criteria. If there's more than one row, it indicates potential FNs due to multiple entries or non-SUDDEN types.
        fn = len(group) - tp
        
        confusion_matrices[(experiment, trace_threshold, anomaly_threshold)] = {'TP': tp, 'FN': fn}



    #print(confusion_matrices)
    #print(total_tp)
    #print(total_fn)

    #accuracy = total_tp / (total_tp + total_fn)
    #print(accuracy)
    # pro tripel average und dann accuracy berechenen
    aggregated_data = {}

    # Loop through each item in the dictionary
    for key, value in confusion_matrices.items():
        trace, anomaly = key[1], key[2]
        ttuple= (trace, anomaly)  # The experiment identifier is the first element of the tuple
        if ttuple not in aggregated_data:
            aggregated_data[ttuple] = {'TP': 0, 'FN': 0}
        aggregated_data[ttuple]['TP'] += value['TP']
        aggregated_data[ttuple]['FN'] += value['FN']

    return aggregated_data
    

dict = calc_accracy(weglassen=False)

def to_matrix(numbers_dict):
    accuracy_dict = {}

    for key, values in numbers_dict.items():
        if (values['TP'] + values['FN']) > 0:  
            accuracy = values['TP'] / (values['TP'] + values['FN'])
        else:
            accuracy = 0 
        accuracy_dict[key] = accuracy
    print(accuracy_dict)
          
to_matrix(dict)   
        



   