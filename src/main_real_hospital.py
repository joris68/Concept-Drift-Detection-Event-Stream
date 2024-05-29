from ModelHandler import ModelHandler
from TraceMapHandler import TraceMapHandler
from ProcessHistory import ProcessHistory
from pybeamline.sources import log_source
import time
import csv
from storage_Handler import upload_blob, download_blob

def offer(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon, size):
    #logging.basicConfig(filename="logs/logs_sudden.log", encoding="utf-8", level=logging.DEBUG)
    my_trace_map_handler = TraceMapHandler(traceMapSize=size)
    my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=allowed_deviation, trace_Treshold=trace_treshold)
    my_process_history = ProcessHistory(my_model_handler, lower_boundary=lower_boundary, anomaly_treshhold=anomaly_treshold, cohens_boundary=cohens_boundary, model_epsilon=model_epsilon)
    log_source("DataImported/Hospital_log.xes").pipe().subscribe(lambda x: my_process_history.concept_Drift_detection(x))
    return len(my_process_history.processHistory), my_process_history.driftHistory, my_process_history.historyCohens 




if __name__ == "__main__":
        download_blob("experiments-data-bucket68", "Hospital_log.xes", "DataImported/hospital.xes"  )
        try:
            with open('./ExperimentsDocker/hospital.csv', 'x',  newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Experiment",  "Dataset", "Deviation", "Trace Threshold",  "Lower Boundary", "Anomaly Threshold" ,"Cohens Boundary", "Model Epsilon",  "Drifts detected", "at event", "exe time", "cohens score", "size"])
        except:
            print("file error occured")

        dataset = "hospital"

        trace_map_sizes = [ 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]

        for size in trace_map_sizes:
                start_time = time.time()
                # Execute the experiment with the current combination of thresholds
                PH_length, drift_history, cohens_history = offer(allowed_deviation=1.0, trace_treshold=0.7, lower_boundary=2500, anomaly_treshold=0.7, cohens_boundary=13, model_epsilon=0.2, size=size)
                execution_time = time.time() - start_time
                try:
                    with open('./ExperimentsDocker/hospital.csv', 'a',  newline='') as file:
                        writer = csv.writer(file)
                        for x in range(min(len(drift_history), len(cohens_history))):
                            writer.writerow([1, dataset, 1.0, 0.7, 2500, 0.7, 13, 0.2, drift_history[x][0], drift_history[x][1], execution_time, cohens_history[x]], size)
                except:
                     print("Error occured in for loop")

        upload_blob("experiments-bucket68", './ExperimentsDocker/hospital.csv', 'hospital.csv')