import pandas as pd

# Replace 'example.csv' with the path to your CSV file
file_path = 'Experiments/experiment_1.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)
values_to_filter = ["sudden_100", "incremental_100", "recurring_100", "gradual_100"]

filtered_df = df[df['Dataset']== "sudden_100"]

grouped_df = filtered_df.groupby(['Experiment', 'Run through', 'Dataset'])


aggregated_df = grouped_df.agg({
    'exe time': 'mean',  # Calculate mean execution time
    'cohens score': 'mean',  # Calculate mean Cohens score
    'Drifts detected': 'count',  # Count the number of drifts detected in each group
}).reset_index()

print(aggregated_df)

selected_cols = filtered_df[["exe time","Drifts detected"]]
print(selected_cols)