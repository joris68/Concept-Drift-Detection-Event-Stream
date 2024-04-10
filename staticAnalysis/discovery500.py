import pm4py

#log = pm4py.read_xes("Data/synth/sudden_time_noise0_500_baseline.xes") 
#net, initial_marking, final_marking = pm4py.discover_petri_net_inductive(log)
#pm4py.view_petri_net(net, initial_marking, final_marking)

log = pm4py.read_xes("Data/synth/sudden_time_noise0_1000_baseline.xes") 
net, initial_marking, final_marking = pm4py.discover_petri_net_inductive(log)
pm4py.view_petri_net(net, initial_marking, final_marking)


