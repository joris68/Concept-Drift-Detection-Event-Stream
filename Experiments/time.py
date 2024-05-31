import pandas as pd
import statistics as s

events_sudden = 1046

events_recurring = 1053

event_gradual = 1118

events_incremental = 1062

def time_sudden():
     file_path = 'ExperimentsDocker/sudden_100.csv'
     df = pd.read_csv(file_path)
     avg_time = df["exe time"].mean()
     time_per_event = avg_time / events_sudden

     print(f"AVG time Sud: {avg_time},  TPE: {time_per_event}")


def time_recurring():
     file_path = 'ExperimentsDocker/recurring_100.csv'
     df = pd.read_csv(file_path)
     avg_time = df["exe time"].mean()
     time_per_event = avg_time / events_recurring

     print(f"AVG time Rec: {avg_time},  TPE: {time_per_event}")

def time_incremental():
     file_path = 'ExperimentsDocker/incremental_100.csv'
     df = pd.read_csv(file_path)
     avg_time = df["exe time"].mean()
     time_per_event = avg_time / events_incremental

     print(f"AVG time Inc: {avg_time},  TPE: {time_per_event}")


def time_gradual():
     file_path = 'ExperimentsDocker/incremental_100.csv'
     df = pd.read_csv(file_path)
     avg_time = df["exe time"].mean()
     time_per_event = avg_time / event_gradual

     print(f"AVG time Grad: {avg_time},  TPE: {time_per_event}")


time_sudden()
time_recurring()
time_incremental()
time_gradual()