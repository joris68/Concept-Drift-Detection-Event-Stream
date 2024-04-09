from ModelHandler import ModelHandler
from TraceMapHandler import TraceMapHandler
from ProcessHistory import ProcessHistory
from pybeamline.sources import log_source, xes_log_source_from_file


def Road_management(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):
    #logging.basicConfig(filename="logs/logs_sudden.log", encoding="utf-8", level=logging.DEBUG)
          my_trace_map_handler = TraceMapHandler(traceMapSize=200)
          my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=allowed_deviation, trace_Treshold=trace_treshold)
          my_process_history = ProcessHistory(my_model_handler, lower_boundary=lower_boundary, anomaly_treshhold=anomaly_treshold, cohens_boundary=cohens_boundary, model_epsilon=model_epsilon)
          log_source("Data/real-world/Road_Traffic_Fine_Management_Process.xes").pipe().subscribe(lambda x: my_process_history.concept_Drift_detection(x))
          print(len(my_process_history.processHistory))
          print(my_process_history.driftHistory)
          print(my_process_history.historyCohens)
          #return len(my_process_history.processHistory), my_process_history.driftHistory, my_process_history.historyCohens

def BPI_challenge(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):
        my_trace_map_handler = TraceMapHandler(traceMapSize=200)
        my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=allowed_deviation, trace_Treshold=trace_treshold)
        my_process_history = ProcessHistory(my_model_handler, lower_boundary=lower_boundary, anomaly_treshhold=anomaly_treshold, cohens_boundary=cohens_boundary, model_epsilon=model_epsilon)
        xes_log_source_from_file("Data/real-world/Road_Traffic_Fine_Management_Process.xes").pipe().subscribe(lambda x: my_process_history.concept_Drift_detection(x))
        print(len(my_process_history.processHistory))
        print(my_process_history.driftHistory)
        print(my_process_history.historyCohens)


if __name__ == "__main__":
    #Road_management(allowed_deviation=1.0, trace_treshold=0.5, lower_boundary=6000, anomaly_treshold=0.7, cohens_boundary=13, model_epsilon=0.2)
    BPI_challenge(allowed_deviation=1.0, trace_treshold=0.5, lower_boundary=6000, anomaly_treshold=0.7, cohens_boundary=13, model_epsilon=0.2)

