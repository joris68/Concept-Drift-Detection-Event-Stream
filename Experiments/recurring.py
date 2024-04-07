import pandas as pd

# Replace 'example.csv' with the path to your CSV file
file_path = 'Experiments/recurring_100.csv'
df = pd.read_csv(file_path)
confusion_matrices = {}

# every rigth drift would depend on the 

for (trace_threshold, anomaly_threshold), group in df.groupby(['Trace Threshold', 'Lower Boundary']):
    
    #first row should be DriftType.SUDDEN
    #second row should be D
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

