from ModelHandler import ModelHandler
from TraceMapHandler import TraceMapHandler
from ProcessHistory import ProcessHistory
from pybeamline.sources import log_source
import time
import csv



def sudden_500(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):
    #logging.basicConfig(filename="logs/logs_sudden.log", encoding="utf-8", level=logging.DEBUG)
    my_trace_map_handler = TraceMapHandler(traceMapSize=40)
    my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=allowed_deviation, trace_Treshold=trace_treshold)
    my_process_history = ProcessHistory(my_model_handler, lower_boundary=lower_boundary, anomaly_treshhold=anomaly_treshold, cohens_boundary=cohens_boundary, model_epsilon=model_epsilon)
    log_source("Data/synth/sudden_time_noise0_500_baseline.xes").pipe().subscribe(lambda x: my_process_history.concept_Drift_detection(x))
    return len(my_process_history.processHistory), my_process_history.driftHistory, my_process_history.historyCohens 


if __name__ == "__main__":
     sudden_500(2.0, 0.8, 400, 0.7, 13, 0.25)


