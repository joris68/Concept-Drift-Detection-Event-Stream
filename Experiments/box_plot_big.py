import pandas as pd
import statistics as s
import seaborn as sns
import matplotlib.pyplot as plt



def calc_latency_sudde():
     file_path = 'ExperimentsDocker/sudden_100.csv'
     df = pd.read_csv(file_path)
     tuple_list = []
    #filter out the true postives and save (MS and event)
     for (experiment, trace_threshold, anomaly_threshold), group in df.groupby(['Experiment','Trace Threshold', 'Anomaly Threshold']):
        counter = 0
        for index, row in group.iterrows():
                if row["Drifts detected"] == "DriftType.SUDDEN" and row["at event"] >= 540 and counter == 0:
                    #tuple_list.append((row["Anomaly Threshold"], row["at event"]))
                    tuple_list.append(row["at event"] - 540)
                    break
                
                counter += 1
     print(f"lentght sudden list {len(tuple_list)}")
     return tuple_list



def calc_latency_recurring():
     file_path = 'ExperimentsDocker/recurring_100.csv'
     df = pd.read_csv(file_path)
     tuple_list = []
    #filter out the true postives and save (MS and event)
     for (experiment, trace_threshold, anomaly_threshold), group in df.groupby(['Experiment','Trace Threshold', 'Anomaly Threshold']):
        counter = 0
        for index, row in group.iterrows():
               if row["Drifts detected"] == "DriftType.SUDDEN" and row["at event"] >= 540 and row['at event'] <= 697 and counter == 0:
                    #tuple_list.append((1, row["Anomaly Threshold"], row["at event"]))
                    tuple_list.append(row["at event"] - 540)
               elif row["Drifts detected"] == "DriftType.SUDDEN_RECURRING" and row["at event"] >= 697 and counter == 1:
                    #tuple_list.append((2, row["Anomaly Threshold"], row["at event"]))
                    tuple_list.append(row["at event"] - 697)
               else:
                    counter += 1
     print(f"length recurring list: {len(tuple_list)}")
     return tuple_list

#calc_latency_recurring()

def calc_latency_gradual():
     file_path = 'ExperimentsDocker/gradual_100.csv'
     df = pd.read_csv(file_path)
     tuple_list = []
    #filter out the true postives and save (MS and event)
     for (experiment, trace_threshold, anomaly_threshold), group in df.groupby(['Experiment','Trace Threshold', 'Anomaly Threshold']):
        counter = 0
        for index, row in group.iterrows():
                if row["Drifts detected"] == "DriftType.SUDDEN" and row["at event"] >= 540 and counter == 0:
                    #tuple_list.append((row["Anomaly Threshold"], row["at event"]))
                    tuple_list.append(row["at event"] -540 )
                    break
                
                counter += 1
     print(f"Lenght gradual List: {len(tuple_list)}")

     return tuple_list


def make_big_box_plot(data1, data2, data3):
     labels = ['Sudden', 'Recurring', 'Gradual']
     ax = sns.boxplot(data=[data1, data2, data3])

     for i, box in enumerate(ax.artists):
          box.set_edgecolor('black')       # Set the border color for each box
          box.set_facecolor('white')       # Set the filling of the box to white

          # Each box has 6 associated Line2D objects (whiskers, caps, and median line)
          # Index 4 is the median line
          median_line = ax.lines[6*i+4]
          median_line.set_color('purple')  # Set the median line color to purple
          median_line.set_linewidth(2) 
     plt.xticks(ticks=range(3), labels=labels)
    # plt.title('Multiple Dataset Boxplot')
     #plt.xlabel('Latency Lag')
     plt.ylabel('Latency Lag')
     plt.show()


data_sudden = calc_latency_sudde()
data_recurring =calc_latency_recurring()
data_gradual = calc_latency_gradual()

make_big_box_plot(data1=data_sudden, data2=data_recurring, data3=data_gradual)