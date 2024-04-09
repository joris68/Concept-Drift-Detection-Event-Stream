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

count_drifts(True)
        



   