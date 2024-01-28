from ModelHandler import ModelHandler
from TraceMapHandler import TraceMapHandler

# this is out main program 

#TODO
# 1. write the main method with the beamline pipeline in here

# TODO Later
# concept drift distinction comes in here

class ProcessHistory:

     def __init__(self, modelHandler : ModelHandler) -> None:
          self.modelHandler = modelHandler
          self.processHistory = []

     def concept_Drift_detection(self, event):
          self.modelHandler.dataStructures.process_new_event(event)

          isAlining = self.modelHandler.check_trace_alignment(self.modelHandler.dataStructures.active_trace_ID)

          if len(self.processHistory) > 0 and (not isAlining):
               
               pass
          else:
               self.modelHandler.mine_new_model(trace_ids=None)

               




#if __name__ == "__main__":
