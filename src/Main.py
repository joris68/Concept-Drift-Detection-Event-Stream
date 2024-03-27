from ModelHandler import ModelHandler
from TraceMapHandler import TraceMapHandler
from ProcessHistory import ProcessHistory
from pybeamline.sources import log_source
from pybeamline.filters import excludes_activity_filter
from DriftTypes import DriftType
from TimeModel import TimeModel
import logging
import pprint
import math
import statistics


if __name__ == "__main__":


     logging.basicConfig(filename='logs/logs_sudden.log', encoding='utf-8', level=logging.DEBUG)

     my_trace_map_handler = TraceMapHandler(traceMapSize=40)

     my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=1.7, trace_Treshold=0.6, model_Treshold=0.7)

     my_process_history = ProcessHistory(my_model_handler, lower_boundary=200, anomaly_treshhold=0.7 , cohens_boundary=12.0)
               
     log_source("Data/synth/sudden_time_noise0_100_baseline.xes").pipe(
    
    
     ).subscribe(lambda x: my_process_history.concept_Drift_detection(x))

     #for model in my_process_history.processHistory:
      #    pprint.pprint(model.times)
      #    print("-------------------------------------------")

    # print(f"this is the length of my Processhistory {len(my_process_history.processHistory)}")