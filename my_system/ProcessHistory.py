from ModelHandler import ModelHandler
from TraceMapHandler import TraceMapHandler
from pybeamline.sources import log_source
from pybeamline.filters import excludes_activity_filter
import logging
#TODO
# 1. write the main method with the beamline pipeline in here
# what is duration mean and std and would I need that for my algo


# TODO Later
# concept drift distinction comes in here

class ProcessHistory:

     def __init__(self, modelHandler : ModelHandler, lower_boundary, anomaly_treshhold) -> None:
          self.modelHandler = modelHandler
          self.processHistory = []
          self.events_lower_boundary = lower_boundary
          #brauch ich das wirklich hier?
          self.anomaly_treshhold = anomaly_treshhold

     def __str__(self) -> str:
          #my_string = ""
         # for model in self.processHistory:
          #     my_string.
          pass

     def concept_Drift_detection(self, event):

          self.modelHandler.dataStructures.process_new_event(event)
          isAlining = self.modelHandler.check_trace_alignment(self.modelHandler.dataStructures.active_trace_ID)
          if len(self.processHistory) > 0 and (not isAlining):
               
               potential_new_model = self.modelHandler.mine_new_model(self.modelHandler.get_not_aligning_trace_ids)
               if self.modelHandler.is_new_model(potential_new_model, self.anomaly_treshhold):
                    self.processHistory.append(potential_new_model)
                    self.modelHandler.active_time_model = potential_new_model
               else:
                    pass
          else:
               if self.modelHandler.dataStructures.processed_events >= self.events_lower_boundary:
                    #mine initial model
                    self.modelHandler.mine_new_model(trace_ids=None)
               else:
                    pass
               
     
     #TODO : Implementation
     def concept_drift_distinction(self):
          pass




if __name__ == "__main__":


     logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
     
     my_trace_map_handler = TraceMapHandler(30)

     my_model_handler = ModelHandler(my_trace_map_handler, 1, 0.8, 0.8)

     my_process_history = ProcessHistory(my_model_handler, 100, 0.8 )
               
     log_source("synthData/recurring_time_noise0_100_baseline.xes").pipe(
    
    
     ).subscribe(lambda x: my_process_history.concept_Drift_detection(x))

     for model in my_process_history.processHistory:
          print(model)



