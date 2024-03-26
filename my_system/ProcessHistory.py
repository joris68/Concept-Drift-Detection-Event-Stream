from ModelHandler import ModelHandler
from TraceMapHandler import TraceMapHandler
from pybeamline.sources import log_source
from pybeamline.filters import excludes_activity_filter
from DriftTypes import DriftType
from TimeModel import TimeModel
import logging
import pprint


class ProcessHistory:

     def __init__(self, modelHandler : ModelHandler, lower_boundary : int, anomaly_treshhold) -> None:
          self.modelHandler = modelHandler
          self.processHistory = []
          self.events_lower_boundary = lower_boundary
          #brauch ich das wirklich hier?
          self.anomaly_treshhold = anomaly_treshhold

          

     def concept_Drift_detection(self, event):

          self.modelHandler.dataStructures.process_new_event(event)
          #isAlining = self.modelHandler.check_trace_alignment(self.modelHandler.dataStructures.active_trace_ID, self.modelHandler.active_time_model)
          
          if len(self.processHistory) > 0:

               isAlining = self.modelHandler.check_trace_alignment(self.modelHandler.dataStructures.active_trace_ID, self.modelHandler.active_time_model)
               logging.info(f"active trace will be conformanced checked : {isAlining}")
               if not isAlining:

                    potential_new_model = self.modelHandler.mine_new_model(self.modelHandler.get_nonfitting_traces_from_traceMap())

                    if self.modelHandler.is_new_Model(potential_new_model, self.anomaly_treshhold):
                         self.processHistory.append(potential_new_model)
                         self.modelHandler.active_time_model = self.processHistory[-1]
                         logging.info("new Model got appended to the process History, and is now active.")

          elif len(self.processHistory) == 0:

               if self.modelHandler.dataStructures.processed_events >= self.events_lower_boundary:
                    #mine initial model
                    initial_timemodel = self.modelHandler.mine_new_model(trace_ids=None)
                    logging.info("Initial timemodel was mined")
                    self.processHistory.append(initial_timemodel)
                    self.modelHandler.active_time_model = self.processHistory[-1]
                    logging.info("Initial timemodel was appended to the history, and is now active")
               
   
     def concept_drift_distinction(self) -> DriftType:
          if len(self.processHistory) <= 1:
               #raise Error("How come we make distinctions?")
               pass
          
          for model in self.processHistory:
               pass
          

     def calculate_modelscore(timemodel : TimeModel):

          pass







if __name__ == "__main__":


     logging.basicConfig(filename='logs/logs_incremental_500.log', encoding='utf-8', level=logging.DEBUG)

     my_trace_map_handler = TraceMapHandler(traceMapSize=40)

     my_model_handler = ModelHandler(my_trace_map_handler, allowed_deviation=1.7, trace_Treshold=0.6, model_Treshold=0.7)

     my_process_history = ProcessHistory(my_model_handler, lower_boundary=200, anomaly_treshhold=0.6 )
               
     log_source("synthData/incremental_time_noise0_100_baseline.xes").pipe(
    
    
     ).subscribe(lambda x: my_process_history.concept_Drift_detection(x))

     for model in my_process_history.processHistory:
          pprint.pprint(model.times)
          print("-------------------------------------------")

     print(f"this is the length of my Processhistory {len(my_process_history.processHistory)}")




