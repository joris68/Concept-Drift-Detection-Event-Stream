import pandas as pd
from pm4py.objects.log.importer.xes import importer as xes_importer

# Define the path to your XES file
xes_file_path = "Data/real-world/Road_Traffic_Fine_Management_Process.xes"

# Define the date format in your XES file
date_format = '%Y-%m-%dT%H:%M:%S%z'

# Read the XES file using pm4py
log = xes_importer.apply(xes_file_path)

# Convert the log to a pandas DataFrame
def convert_to_dataframe(log):
    data = []
    for trace in log:
        for event in trace:
            #event_dict = event.copy()
            event_dict = {}
            event_dict['case:concept:name'] = trace.attributes['concept:name']
            data.append(event_dict)
    df = pd.DataFrame(data)
    return df

# Convert the EventLog to a DataFrame
df = convert_to_dataframe(log)

# Specify the format for the timestamp column and convert to datetime
timestamp_key = 'time:timestamp'
if timestamp_key in df.columns:
    df[timestamp_key] = pd.to_datetime(df[timestamp_key], format=date_format, utc=True)

# Sort the DataFrame by the timestamp column if needed
df = df.sort_values(by=[timestamp_key])

# Display the DataFrame
print(df)