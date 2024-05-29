import pandas as pd
import statistics as s

def calc_accuracy():
    file_path = 'ExperimentsDocker/incremental_100.csv'
    df = pd.read_csv(file_path)
    numbers_and_drifts = {}

    for (experiment, trace_threshold, anomaly_threshold), group in df.groupby(['Experiment','Deviation', 'Cohens Boundary']):
        # Initialize a dictionary to store counts of each drift type
        drift_counts = {
            'DriftType.SUDDEN': 0,
            'DriftType.RECURRING': 0,
            'DriftType.INCREMENTAL': 0,
            'DriftType.SUDDEN_RECURRING': 0,
            'DriftType.INCREMENTAL_RECURRING': 0,
            'TOTAL': 0
        }

        # Iterate through each row in the group to count drift types
        for index, row in group.iterrows():
            drift_type = row["Drifts detected"]
            if drift_type in drift_counts:
                drift_counts[drift_type] += 1

        # Update the total drifts count
        drift_counts['TOTAL'] = len(group)

        # Save to the dictionary using (experiment, trace_threshold, anomaly_threshold) as key
        numbers_and_drifts[(experiment, trace_threshold, anomaly_threshold)] = drift_counts

    return numbers_and_drifts

# I want the number of drifts for different type of deviations, no matter which
def count_rows_per_group():
    file_path = 'ExperimentsDocker/incremental_100.csv'
    df = pd.read_csv(file_path)
    numbers_and_drifts = {}
    df_one_experiment = df[df["Experiment"]== 0]
    for x in [0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2]:

        df_dev = df_one_experiment[df_one_experiment["Deviation"]== x]
        print(len(df_dev) / 11)

#count_rows_per_group()

def analyze_cohens():
    file_path = 'ExperimentsDocker/incremental_100.csv'
    df = pd.read_csv(file_path)
    df_one_experiment = df[df["Experiment"]== 0]
    for x in [6, 8, 10, 12, 14, 16, 18, 20]:
        df_one_experiment

def calc_accuracy_2():
    file_path = 'ExperimentsDocker/incremental_100.csv'
    df = pd.read_csv(file_path)
    numbers_and_drifts = {}

    for (experiment, deviation), group in df.groupby(['Experiment','Deviation']):
        # Initialize a dictionary to store counts of each drift type
        drift_counts = {
            'DriftType.SUDDEN': 0,
            'DriftType.RECURRING': 0,
            'DriftType.INCREMENTAL': 0,
            'DriftType.SUDDEN_RECURRING': 0,
            'DriftType.INCREMENTAL_RECURRING': 0,
            'TOTAL': 0
        }

        # Iterate through each row in the group to count drift types
        for index, row in group.iterrows():
            drift_type = row["Drifts detected"]
            if drift_type in drift_counts:
                drift_counts[drift_type] += 1

        # Update the total drifts count
        drift_counts['TOTAL'] = len(group)

        # Save to the dictionary using (experiment, trace_threshold, anomaly_threshold) as key
        numbers_and_drifts[(experiment, deviation)] = drift_counts

    return numbers_and_drifts





def aggregate(accs : dict) -> dict:

    aggregation = {}

    for key, value in accs.items():
        key_1 = key[1]
        key_2 = key[2]
        my_tuple = (key_1, key_2)
        if my_tuple not in aggregation:
            aggregation[my_tuple] = drift_counts = {
            'DriftType.SUDDEN': 0,
            'DriftType.RECURRING': 0,
            'DriftType.INCREMENTAL': 0,
            'DriftType.SUDDEN_RECURRING': 0,
            'DriftType.INCREMENTAL_RECURRING': 0,
            'TOTAL': 0
        }
        else:
            aggregation[my_tuple]['DriftType.SUDDEN'] += value['DriftType.SUDDEN']
            aggregation[my_tuple]['DriftType.RECURRING'] += value['DriftType.RECURRING']
            aggregation[my_tuple]['DriftType.INCREMENTAL'] += value['DriftType.INCREMENTAL']
            aggregation[my_tuple]['DriftType.SUDDEN_RECURRING'] += value["DriftType.SUDDEN_RECURRING"]
            aggregation[my_tuple]['DriftType.INCREMENTAL_RECURRING'] += value['DriftType.INCREMENTAL_RECURRING']
            aggregation[my_tuple]['TOTAL'] += value['TOTAL']
    
    return aggregation



def auswahl(drifttype, dict_data):
    to_return = {}
    for key, value in dict_data.items():
        if key not in to_return:
            to_return[key] = value[drifttype]
    
    return to_return

#accuracy_results = calc_accuracy()
#agss = aggregate(accuracy_results)
#agss_auswahl = auswahl('TOTAL', agss)
#print(agss_auswahl)
