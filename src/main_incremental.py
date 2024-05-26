from ModelHandler import ModelHandler
from TraceMapHandler import TraceMapHandler
from ProcessHistory import ProcessHistory
from pybeamline.sources import log_source
import time
import csv
from storage_Handler import upload_blob


def incremental_100(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):
    #logging.basicConfig(filename="logs/logs_incremental.log", encoding="utf-8", level=logging.DEBUG)
    my_trace_map_handler = TraceMapHandler(traceMapSize=40)
    my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=allowed_deviation, trace_Treshold=trace_treshold)
    my_process_history = ProcessHistory(my_model_handler, lower_boundary=lower_boundary, anomaly_treshhold=anomaly_treshold, cohens_boundary=cohens_boundary, model_epsilon=model_epsilon)
    log_source("Data/synth/incremental_time_noise0_100_baseline.xes").pipe().subscribe(lambda x: my_process_history.concept_Drift_detection(x))
    return len(my_process_history.processHistory), my_process_history.driftHistory, my_process_history.historyCohens 




if __name__ == "__main__":


    try:
        with open('./ExperimentsDocker/incremental_100.csv', 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Experiment", "Dataset", "Deviation", "Trace Threshold", "Lower Boundary", "Anomaly Threshold", "Cohens Boundary", "Model Epsilon", "Drifts detected", "at event", "exe time", "cohens score"])
    except:
        print("file error occurred at the beginning")
    

    dataset = "incremental_100"

    cohens = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]  
    deviations = [0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2] 

    for counter_1 in range(0,10):
        for cohen in cohens:
            for dev in deviations:
                    start_time = time.time()
                    # Execute the experiment with the current combination of thresholds
                    PH_length, drift_history, cohens_history = incremental_100(allowed_deviation=dev, trace_treshold=0.6, lower_boundary=220, anomaly_treshold=0.7, cohens_boundary=cohen, model_epsilon=0.2)
                    execution_time = time.time() - start_time
                    try:
                        with open('./ExperimentsDocker/incremental_100.csv', 'w',  newline='') as file:
                            writer = csv.writer(file)
                            if len(drift_history) == 0:
                                writer.writerow([counter_1, dataset, dev, 0.6, 220, 0.7, cohen, 0.2, "NO DRIFT", 0, execution_time, cohens_history[x]])
                            else:
                                for x in range(min(len(drift_history), len(cohens_history))):
                                    writer.writerow([counter_1, dataset, dev, 0.6, 220, 0.7, cohen, 0.2, drift_history[x][0], drift_history[x][1], execution_time, cohens_history[x]])
                    except:
                        print("Error in the forloop")

    upload_blob("experiments-bucket68", './ExperimentsDocker/incremental_100.csv', 'incremental_100.csv')