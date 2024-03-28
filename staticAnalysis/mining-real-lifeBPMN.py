
import pm4py


log = pm4py.read_xes("data\sudden_time_noise0_100_baseline.xes")


bpmn= pm4py.discover_bpmn_inductive(log)

#pm4py.visualization.bpmn.visualizer.save(bpmn, "synthetic_bpmn.bpmn")
pm4py.view_bpmn(bpmn)
