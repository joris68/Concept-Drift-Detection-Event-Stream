import pandas as pd

# actual drift point sudden: 540

# first Point 341, recurring
# second point 697, recurring

actual_drift_point_sudden = 540


def delay_correlation_sudden():
     file_path = 'ExperimentsDocker/sudden_100.csv'
     df = pd.read_csv(file_path)

     grouped_df = df.groupby(['Trace Threshold', 'Lower Boundary']).first().reset_index()

     selected = grouped_df[['Trace Threshold', 'Lower Boundary', 'at event', 'Dataset']]

     grouped_df['delay'] = selected.apply(lambda row: abs(row['at event'] - actual_drift_point_sudden), axis=1)

     #print(grouped_df.head())

     corr = grouped_df['Lower Boundary'].corr(grouped_df['delay'], method='pearson')
     corr2 = grouped_df['Trace Threshold'].corr(grouped_df['delay'],method='pearson')
     print(corr)
     print(corr2)



delay_correlation_sudden()


