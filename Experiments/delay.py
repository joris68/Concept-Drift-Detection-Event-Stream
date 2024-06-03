import pandas as pd

# detection delay only for the True positives!!!

actual_drift_point_sudden = 540

first_point_recurring = 341
second_point_recurring = 697


def delay_correlation_sudden():
     file_path = 'New/sudden_100.csv'
     df = pd.read_csv(file_path)

     grouped_df = df.groupby(["Experiment" ,'Trace Threshold', 'Anomaly Threshold']).first().reset_index()

     selected = grouped_df[['Trace Threshold', 'Lower Boundary', 'at event', 'Dataset']]

     grouped_df['delay'] = selected.apply(lambda row: abs(row['at event'] - actual_drift_point_sudden), axis=1)

     average_delay = grouped_df['delay'].mean()
     std_delay = grouped_df['delay'].std()

     print("Average Delay:", average_delay)
     print("Standard Deviation of Delay:", std_delay)

     return average_delay, std_delay

     #print(grouped_df.head())

     #corr = grouped_df['Lower Boundary'].corr(grouped_df['delay'], method='pearson')
     #corr2 = grouped_df['Trace Threshold'].corr(grouped_df['delay'],method='pearson')
     #print(corr)
     #print(corr2)



def delay_correlation_sudden():
     file_path = 'New/recurring_100.csv'
     df = pd.read_csv(file_path)

     grouped_df = df.groupby(["Experiment" ,'Trace Threshold', 'Anomaly Threshold']).first().reset_index()

     selected = grouped_df[['Trace Threshold', 'Lower Boundary', 'at event', 'Dataset']]





sudden_average, sudden_std = delay_correlation_sudden()


