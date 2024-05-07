import pandas as pd

# Load the data
file_path = 'New/incremental_100.csv'
df = pd.read_csv(file_path)

# Dictionary to store counts
count_dict = {}
# Dictionary to store averages for each Trace Threshold and Anomaly Threshold
average_dict = {}

# Group by 'Experiment', 'Trace Threshold', and 'Anomaly Threshold' and count entries
for (experiment, trace_threshold, anomaly_threshold), group in df.groupby(['Experiment', 'Trace Threshold', 'Anomaly Threshold']):
    # Create a key as a tuple of trace_threshold and anomaly_threshold, accumulate counts
    key = (trace_threshold, anomaly_threshold)
    if key not in count_dict:
        count_dict[key] = []
    count_dict[key].append(len(group))

# Calculate averages for each Trace Threshold and Anomaly Threshold combination
for key, counts in count_dict.items():
    average_dict[key] = sum(counts) / len(counts) if counts else 0

# Print out the average dictionary
print(average_dict)
