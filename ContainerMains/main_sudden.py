from src import ModelHandler
from src import TraceMapHandler
from src import ProcessHistory
from pybeamline.sources import log_source
import time
import csv



def sudden_100(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):
    #logging.basicConfig(filename="logs/logs_sudden.log", encoding="utf-8", level=logging.DEBUG)
    my_trace_map_handler = TraceMapHandler(traceMapSize=40)
    my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=allowed_deviation, trace_Treshold=trace_treshold)
    my_process_history = ProcessHistory(my_model_handler, lower_boundary=lower_boundary, anomaly_treshhold=anomaly_treshold, cohens_boundary=cohens_boundary, model_epsilon=model_epsilon)
    log_source("Data/synth/sudden_time_noise0_100_baseline.xes").pipe().subscribe(lambda x: my_process_history.concept_Drift_detection(x))
    return len(my_process_history.processHistory), my_process_history.driftHistory, my_process_history.historyCohens 




if __name__ == "__main__":


    with open('ExperimentsDocker/sudden_100.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Experiment",  "Dataset", "Deviation", "Trace Threshold",  "Lower Boundary", "Anomaly Threshold" ,"Cohens Boundary", "Model Epsilon",  "Drifts detected", "at event", "exe time", "cohens score"])

        dataset = "sudden_100"

        trace_thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]  
        anomaly_thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] 

        for counter_1 in range(0,10):
            for trace_threshold in trace_thresholds:
                for anomaly_threshold in anomaly_thresholds:
                    start_time = time.time()
                    # Execute the experiment with the current combination of thresholds
                    PH_length, drift_history, cohens_history = sudden_100(allowed_deviation=2.0, trace_treshold=trace_threshold, lower_boundary=220, anomaly_treshold=anomaly_threshold, cohens_boundary=13, model_epsilon=0.2)
                    execution_time = time.time() - start_time
                    
                    for x in range(min(len(drift_history), len(cohens_history))):
                        writer.writerow([counter_1, dataset, 2.0, trace_threshold, 220, anomaly_threshold, 13, 0.2, drift_history[x][0], drift_history[x][1], execution_time, cohens_history[x]])

