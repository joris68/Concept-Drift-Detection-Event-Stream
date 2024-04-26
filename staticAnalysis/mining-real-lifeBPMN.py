
import pm4py


log = pm4py.read_xes("Data\synth\sudden_time_noise0_500_baseline.xes")


bpmn= pm4py.discover_bpmn_inductive(log)

#pm4py.visualization.bpmn.visualizer.save(bpmn, "synthetic_bpmn.bpmn")
pm4py.view_bpmn(bpmn)
