from ModelHandler import ModelHandler
from TraceMapHandler import TraceMapHandler
from ProcessHistory import ProcessHistory
from pybeamline.sources import log_source
import csv
from logger import CSVLogHandler


def main():
     with open('logs/log.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["case", "ActivityName", "class", "Time"])
        print('written')
     
     CSVlogger = CSVLogHandler('logs/log.csv')
     log = CSVlogger.setup_logger('example_logger', 'logs/log.csv')

     my_trace_map_handler = TraceMapHandler(40, log)
     my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=2.0, trace_Treshold=0.7)
     my_process_history = ProcessHistory(my_model_handler, lower_boundary=220, anomaly_treshhold=0.7, cohens_boundary=13, model_epsilon=0.2)
     log_source("Data/synth/sudden_time_noise0_100_baseline.xes").pipe().subscribe(lambda x: my_process_history.concept_Drift_detection(x))

if __name__ == '__main__':
    main()

