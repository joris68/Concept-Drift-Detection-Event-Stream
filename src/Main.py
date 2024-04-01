from ModelHandler import ModelHandler
from TraceMapHandler import TraceMapHandler
from ProcessHistory import ProcessHistory
from pybeamline.sources import log_source
import logging


def setup_loggers(path_detailed, path_output, type):
    high_level_logger = logging.getLogger("high_level_" + type)
    detailed_logger = logging.getLogger("detailed_" + type)

    high_level_logger.setLevel(logging.INFO)
    detailed_logger.setLevel(logging.DEBUG)

    high_handler = logging.FileHandler(path_output, "w", "utf-8")
    detailed_handler = logging.FileHandler(path_detailed, "w", "utf-8")

    # creating a csv logger
    formatter_detailed = logging.Formatter("%(asctime)s, %(levelname)s, %(message)s")
    formatter_output = logging.Formatter("%(asctime)s, %(levelname)s, %(message)s")
    # high_handler.setFormatter(formatter)
    # detailed_handler.setFormatter(formatter)

    # Add handlers to the logger
    high_level_logger.addHandler(high_handler)
    detailed_logger.addHandler(detailed_handler)


def sudden_100(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):

    logging.basicConfig(
        filename="logs/logs_sudden.log", encoding="utf-8", level=logging.DEBUG
    )

    my_trace_map_handler = TraceMapHandler(traceMapSize=40)

    my_model_handler = ModelHandler(
        my_trace_map_handler,
        allowed_deviation=1.7,
        trace_Treshold=0.6,
    )

    my_process_history = ProcessHistory(
        my_model_handler,
        lower_boundary=200,
        anomaly_treshhold=0.7,
        cohens_boundary=12.0,
        model_epsilon=0.3,
    )

    log_source("Data/synth/sudden_time_noise0_100_baseline.xes").pipe().subscribe(
        lambda x: my_process_history.concept_Drift_detection(x)
    )


def incremental_100(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):

    logging.basicConfig(
        filename="logs/logs_incremental.log", encoding="utf-8", level=logging.DEBUG
    )

    my_trace_map_handler = TraceMapHandler(traceMapSize=40)

    my_model_handler = ModelHandler(
        my_trace_map_handler,
        allowed_deviation=1.7,
        trace_Treshold=0.6,
    )

    my_process_history = ProcessHistory(
        my_model_handler,
        lower_boundary=200,
        anomaly_treshhold=0.7,
        cohens_boundary=12.0,
        model_epsilon=0.3,
    )

    log_source("Data/synth/incremental_time_noise0_100_baseline.xes").pipe().subscribe(
        lambda x: my_process_history.concept_Drift_detection(x)
    )


def recurring_100(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):
    logging.basicConfig(
        filename="logs/logs_recurring.log", encoding="utf-8", level=logging.DEBUG
    )

    my_trace_map_handler = TraceMapHandler(traceMapSize=40)

    my_model_handler = ModelHandler(
        my_trace_map_handler,
        allowed_deviation=1.7,
        trace_Treshold=0.6,
    )

    my_process_history = ProcessHistory(
        my_model_handler,
        lower_boundary=200,
        anomaly_treshhold=0.7,
        cohens_boundary=12.0,
        model_epsilon=0.3,
    )

    log_source("Data/synth/recurring_time_noise0_100_baseline.xes").pipe().subscribe(
        lambda x: my_process_history.concept_Drift_detection(x)
    )


def gradual_100(allowed_deviation, trace_treshold, lower_boundary, anomaly_treshold, cohens_boundary, model_epsilon):
    logging.basicConfig(
        filename="logs/logs_gradual.log", encoding="utf-8", level=logging.DEBUG
    )

    my_trace_map_handler = TraceMapHandler(traceMapSize=40)

    my_model_handler = ModelHandler(
        my_trace_map_handler,
        allowed_deviation=1.7,
        trace_Treshold=0.6,
    )

    my_process_history = ProcessHistory(
        my_model_handler,
        lower_boundary=200,
        anomaly_treshhold=0.7,
        cohens_boundary=12.0,
        model_epsilon=0.3,
    )

    log_source("Data/synth/recurring_time_noise0_100_baseline.xes").pipe().subscribe(
        lambda x: my_process_history.concept_Drift_detection(x)
    )


if __name__ == "__main__":

    

    sudden_100()
    incremental_100()
    recurring_100()
    gradual_100()
