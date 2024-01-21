from playGround.TraceMapHandlerBEvent import TraceMapHandlerBEvent

# this class should do the Model handling
# tasks:
#    - mine a new Model from a given set of traces in the TraceMap
#    - calculate the timespreads from an ACTIVE trace
#    - checks if there are any new directly follows relations, if so updates the TimeModel accordingly

class ModelHandler:

     def __init__(self, dataStructures :  TraceMapHandlerBEvent) -> None:
          self.dataStructures = dataStructures
          #self.directly_follows_relations = dict()

     
     def mine_new_model(self):
          pass

     #for a given Trace and a given TimeModel
     def check_activ_trace_alignment():
          pass
     
     # for a given Trace
     def calc_time_spreads():
          pass