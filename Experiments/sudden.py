import pandas as pd

# Replace 'example.csv' with the path to your CSV file
file_path = 'Experiments/sudden_100.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)


# Calculating confusion matrix elements
confusion_matrices = {}

for (trace_threshold, anomaly_threshold), group in df.groupby(['Trace Threshold', 'Lower Boundary']):
    tp = group['Drifts detected'].eq('DriftType.SUDDEN').sum()
    # FN is calculated based on the provided criteria. If there's more than one row, it indicates potential FNs due to multiple entries or non-SUDDEN types.
    fn = len(group) - tp
    
    confusion_matrices[(trace_threshold, anomaly_threshold)] = {'TP': tp, 'FN': fn}


# Summing up the values from the confusion matrix
total_tp = sum(cm['TP'] for cm in confusion_matrices.values())
total_fn = sum(cm['FN'] for cm in confusion_matrices.values())

print(total_tp)
print(total_fn)

