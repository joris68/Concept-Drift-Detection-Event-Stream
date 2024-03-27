import pm4py
import pandas as pd

log = pd.read_csv("data/sudden_time_noise0_100_baseline.csv")

event_log = pm4py.format_dataframe(log, case_id="case", activity_key="event", timestamp_key="startTime" )

#dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)
#print(dfg)
#pm4py.view_dfg(dfg, start_activities, end_activities)
footprints = pm4py.discover_footprints(event_log)
print(footprints)

#trans = pm4py.discover_transition_system(event_log)

pm4py.vis.view_footprints(footprints)


#pm4py.vis.view_transition_system(trans)

#print(footprints)
##pm4py.vis.view_events_distribution_graph(event_log)
#pm4py.vis.view_case_duration_graph(event_log)
#pm4py.vis.view_events_per_time_graph(event_log)
#pm4py.vis.view_performance_spectrum(event_log)

#processtree = pm4py.discovery.discover_process_tree_inductive(event_log)
#pm4py.vis.view_process_tree(processtree)