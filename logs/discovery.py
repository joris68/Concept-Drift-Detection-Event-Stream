import pm4py
import pandas as pd


log = pd.read_csv("logs/log.csv")
log['case'] = log['case'].astype(str)
event_log = pm4py.format_dataframe(log, case_id="case", activity_key="ActivityName", timestamp_key="Time" )
net, initial_marking, final_marking = pm4py.discover_petri_net_inductive(log)
pm4py.view_petri_net(net, initial_marking, final_marking)