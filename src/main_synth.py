from ModelHandler import ModelHandler
from TraceMapHandler import TraceMapHandler
from ProcessHistory import ProcessHistory
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


def recurring_100(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):
    #logging.basicConfig(filename="logs/logs_recurring.log", encoding="utf-8", level=logging.DEBUG)
    my_trace_map_handler = TraceMapHandler(traceMapSize=40)
    my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=allowed_deviation, trace_Treshold=trace_treshold)
    my_process_history = ProcessHistory(my_model_handler, lower_boundary=lower_boundary, anomaly_treshhold=anomaly_treshold, cohens_boundary=cohens_boundary, model_epsilon=model_epsilon)
    log_source("Data/synth/recurring_time_noise0_100_baseline.xes").pipe().subscribe(lambda x: my_process_history.concept_Drift_detection(x))
    return len(my_process_history.processHistory), my_process_history.driftHistory, my_process_history.historyCohens


def gradual_100(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):
    #logging.basicConfig(filename="logs/logs_gradual.log", encoding="utf-8", level=logging.DEBUG)
    my_trace_map_handler = TraceMapHandler(traceMapSize=40)
    my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=allowed_deviation, trace_Treshold=trace_treshold)
    my_process_history = ProcessHistory(my_model_handler, lower_boundary=lower_boundary, anomaly_treshhold=anomaly_treshold, cohens_boundary=cohens_boundary, model_epsilon=model_epsilon)
    log_source("Data/synth/gradual_time_noise0_100_baseline.xes").pipe().subscribe(lambda x: my_process_history.concept_Drift_detection(x))
    return len(my_process_history.processHistory), my_process_history.driftHistory, my_process_history.historyCohens


def incremental_100(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):
    #logging.basicConfig(filename="logs/logs_incremental.log", encoding="utf-8", level=logging.DEBUG)
    my_trace_map_handler = TraceMapHandler(traceMapSize=40)
    my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=allowed_deviation, trace_Treshold=trace_treshold)
    my_process_history = ProcessHistory(my_model_handler, lower_boundary=lower_boundary, anomaly_treshhold=anomaly_treshold, cohens_boundary=cohens_boundary, model_epsilon=model_epsilon)
    log_source("Data/synth/incremental_time_noise0_100_baseline.xes").pipe().subscribe(lambda x: my_process_history.concept_Drift_detection(x))
    return len(my_process_history.processHistory), my_process_history.driftHistory, my_process_history.historyCohens

if __name__ == "__main__":


    with open('ExperimentsDocker/recurring_100.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Experiment",  "Dataset", "Deviation", "Trace Threshold", "Anomaly Threshold", "Lower Boundary",  "Cohens Boundary", "Model Epsilon", "Drift Actual", "Drifts detected", "at event", "at event actual", "exe time", "cohens score"])

        Experiment = 1
        # Assuming datasets list is defined as shown in your snippet
        datasets = ["recurring_100"]
        experiments_1 = [recurring_100]

        trace_thresholds = [0.8, 0.7, 0.6, 0.5]  
        anomaly_thresholds = [0.8, 0.7, 0.6, 0.5]  

        for counter_1, experiment in enumerate(experiments_1):
            for trace_threshold in trace_thresholds:
                for anomaly_threshold in anomaly_thresholds:
                    start_time = time.time()
                    # Execute the experiment with the current combination of thresholds
                    PH_length, drift_history, cohens_history = experiment(allowed_deviation=2.0, trace_treshold=trace_threshold, lower_boundary=220, anomaly_treshold=anomaly_threshold, cohens_boundary=13, model_epsilon=0.2)
                    execution_time = time.time() - start_time
                    
                    for x in range(len(drift_history)):
                        writer.writerow([Experiment, datasets[counter_1], 2.0, trace_threshold, 220, anomaly_threshold, 11, 0.2, 1, drift_history[x][0], drift_history[x][1], 0, execution_time, cohens_history[x]])



    with open('ExperimentsDocker/sudden_100.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Experiment",  "Dataset", "Deviation", "Trace Threshold", "Anomaly Threshold", "Lower Boundary",  "Cohens Boundary", "Model Epsilon", "Drift Actual", "Drifts detected", "at event", "at event actual", "exe time", "cohens score"])

        Experiment = 1
        # Assuming datasets list is defined as shown in your snippet
        datasets = ["sudden_100"]
        experiments_1 = [sudden_100]

        trace_thresholds = [0.8, 0.7, 0.6, 0.5]  
        anomaly_thresholds = [0.8, 0.7, 0.6, 0.5]  

        for counter_1, experiment in enumerate(experiments_1):
            for trace_threshold in trace_thresholds:
                for anomaly_threshold in anomaly_thresholds:
                    start_time = time.time()
                    # Execute the experiment with the current combination of thresholds
                    PH_length, drift_history, cohens_history = experiment(allowed_deviation=2.0, trace_treshold=trace_threshold, lower_boundary=220, anomaly_treshold=anomaly_threshold, cohens_boundary=13, model_epsilon=0.2)
                    execution_time = time.time() - start_time
                    
                    for x in range(len(drift_history)):
                        writer.writerow([Experiment, datasets[counter_1], 2.0, trace_threshold, 220, anomaly_threshold, 11, 0.2, 1, drift_history[x][0], drift_history[x][1], 0, execution_time, cohens_history[x]])


    ########################################################################

    with open('ExperimentsDocker/incremental_100.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Experiment",  "Dataset", "Deviation", "Trace Threshold", "Anomaly Threshold", "Lower Boundary",  "Cohens Boundary", "Model Epsilon", "Drift Actual", "Drifts detected", "at event", "at event actual", "exe time", "cohens score"])

        Experiment = 1
        # Assuming datasets list is defined as shown in your snippet
        datasets = ["incremental_100"]
        experiments_1 = [incremental_100]

        trace_thresholds = [0.8, 0.7, 0.6, 0.5]  
        anomaly_thresholds = [0.8, 0.7, 0.6, 0.5]  

        for counter_1, experiment in enumerate(experiments_1):
            for trace_threshold in trace_thresholds:
                for anomaly_threshold in anomaly_thresholds:
                    start_time = time.time()
                    # Execute the experiment with the current combination of thresholds
                    PH_length, drift_history, cohens_history = experiment(allowed_deviation=2.0, trace_treshold=trace_threshold, lower_boundary=220, anomaly_treshold=anomaly_threshold, cohens_boundary=13, model_epsilon=0.2)
                    execution_time = time.time() - start_time
                    
                    for x in range(len(drift_history)):
                        writer.writerow([Experiment, datasets[counter_1], 2.0, trace_threshold, 220, anomaly_threshold, 11, 0.2, 1, drift_history[x][0], drift_history[x][1], 0, execution_time, cohens_history[x]])


    with open('ExperimentsDocker/gradual_100.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Experiment",  "Dataset", "Deviation", "Trace Threshold", "Anomaly Threshold", "Lower Boundary",  "Cohens Boundary", "Model Epsilon", "Drift Actual", "Drifts detected", "at event", "at event actual", "exe time", "cohens score"])

        Experiment = 1
        # Assuming datasets list is defined as shown in your snippet
        datasets = ["gradual_100"]
        experiments_1 = [gradual_100]

        trace_thresholds = [0.8, 0.7, 0.6, 0.5]  
        anomaly_thresholds = [0.8, 0.7, 0.6, 0.5]  

        for counter_1, experiment in enumerate(experiments_1):
            for trace_threshold in trace_thresholds:
                for anomaly_threshold in anomaly_thresholds:
                    start_time = time.time()
                    # Execute the experiment with the current combination of thresholds
                    PH_length, drift_history, cohens_history = experiment(allowed_deviation=2.0, trace_treshold=trace_threshold, lower_boundary=220, anomaly_treshold=anomaly_threshold, cohens_boundary=13, model_epsilon=0.2)
                    execution_time = time.time() - start_time
                    
                    for x in range(len(drift_history)):
                        writer.writerow([Experiment, datasets[counter_1], 2.0, trace_threshold, 220, anomaly_threshold, 11, 0.2, 1, drift_history[x][0], drift_history[x][1], 0, execution_time, cohens_history[x]])


