from ModelHandler import ModelHandler
from TraceMapHandler import TraceMapHandler
from ProcessHistory import ProcessHistory
from pybeamline.sources import log_source
import time
import csv
import pandas as pd
import pm4py
from pm4py.objects.log.importer.xes import importer as xes_importer


def sudden_100(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):
    #logging.basicConfig(filename="logs/logs_sudden.log", encoding="utf-8", level=logging.DEBUG)
    my_trace_map_handler = TraceMapHandler(traceMapSize=40)
    my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=allowed_deviation, trace_Treshold=trace_treshold)
    my_process_history = ProcessHistory(my_model_handler, lower_boundary=lower_boundary, anomaly_treshhold=anomaly_treshold, cohens_boundary=cohens_boundary, model_epsilon=model_epsilon)
    log_source("Data/synth/sudden_time_noise0_100_baseline.xes").pipe().subscribe(lambda x: my_process_history.concept_Drift_detection(x))
    return len(my_process_history.processHistory), my_process_history.driftHistory, my_process_history.historyCohens 

def fine_management_100(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):
     #logging.basicConfig(filename="logs/logs_sudden.log", encoding="utf-8", level=logging.DEBUG)
     my_trace_map_handler = TraceMapHandler(traceMapSize=200)
     my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=allowed_deviation, trace_Treshold=trace_treshold)
     my_process_history = ProcessHistory(my_model_handler, lower_boundary=lower_boundary, anomaly_treshhold=anomaly_treshold, cohens_boundary=cohens_boundary, model_epsilon=model_epsilon)

     #xes_file_path = "Data/real-world/Road_Traffic_Fine_Management_Process.xes"
     xes_file_path = "Data/real-world/Road_Traffic_Fine_Management_Process.xes"

     #log = xes_importer.apply(xes_file_path, variant=v, parameters=parameters)

     # Define the date format in your XES file
     date_format = '%Y-%m-%dT%H:%M:%S%z'

     log = pm4py.read_xes(xes_file_path, format=date_format)

     #df = pd.DataFrame(log)
     #df.head()

     log_source(log).pipe().subscribe(lambda x: my_process_history.concept_Drift_detection(x))
     return len(my_process_history.processHistory), my_process_history.driftHistory, my_process_history.historyCohens 


if __name__== "__main__":
    
    #PH_length, drift_history, cohens_history = sudden_100(allowed_deviation=2.0, trace_treshold=0.5, lower_boundary=220, anomaly_treshold=0.7, cohens_boundary=13, model_epsilon=0.2)

    fine_management_100(allowed_deviation=1.0, trace_treshold=0.7, lower_boundary=2500, anomaly_treshold=0.8, cohens_boundary=13, model_epsilon=0.2)