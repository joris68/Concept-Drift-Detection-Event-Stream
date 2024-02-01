from TraceMapHandler import TraceMapHandler
from TimeModel import TimeModel
import statistics

# TODO
#1. einen model score einbauen.


class ModelHandler:

     def __init__(self, dataStructures :  TraceMapHandler, allowed_deviation, trace_Treshold, model_Treshold) -> None:
          self.dataStructures = dataStructures
          # will be initialized with None until the first time model is derived
          self.active_time_model = None

          # handels the outlier counter for the active model (the latest in the process history)
          #self.outlier_Counter = 0
          # we will start with +- 1 Std from the mean and where we stand
          self.allowed_deviation = allowed_deviation

          # we will define a treshhold if a trace fits the model, we will define if 80% of the the realtions in the 
          self.trace_Treshold = trace_Treshold
          self.model_Treshold = model_Treshold



     # hier weichen wir bewusst von der Normal implementation ab. Wir brauchen hier einen anomalie threshold, wei wir das model davor nur mit den 
     def is_new_Model(self, timemodel : TimeModel, anomaly_treshhold) -> bool:
          
          return True



     # there are two situations where we have to mine a model
     # 1. we found a trace non-fitting, we will use only unfitting traces of the current window
     # 2. there is no process model, yet so we have to define to define the first
               # hier vielleicht mir vorlaufzeit, also erst nachdem 100 events geprocessed wurden dann wird das erste TimeModel minen
          
     def mine_new_model(self, trace_ids = None) -> TimeModel:
          calc_dic = self.__set_to_dict()

          if trace_ids is None:
               # initial model -> all traces in the tarcemap
               trace_ids = self.dataStructures.traceMap.keys()
          
          for t in trace_ids:
               trace_spreads = self.__calc_time_spreads(t)

               for relation in trace_spreads.keys():
                    if relation in calc_dic:
                         calc_dic[relation].append(trace_spreads[relation])
                    else:
                         pass
                         #raise Exception("something went terrible wrong with the directly follows relationhip in mining a new model")
          
          return self.__calc_dic_to_TimeModel(calc_dic)

     
     
     def __calc_dic_to_TimeModel(self, calc_dic : dict)-> TimeModel:

          timemodel_dict = dict()
          
          for r in calc_dic.keys():
               # hier try error wegen std udn soooo
               try:
                    avg = statistics.mean(calc_dic[r])
               except:
                    avg = 0
               try: # for the case that there is only one element in a list
                    std = statistics.stdev(calc_dic[r])
               except:
                    std = 0

               timemodel_dict[r] = [avg, std]

          timemodel = TimeModel(timemodel_dict)
          return timemodel
  
     
     def __set_to_dict(self) -> dict:
          tuple_set = self.dataStructures.directly_follows_relations
          my_dict = dict()
          for t in tuple_set:
               my_dict[t] = [] ## assigning empty list to aggreate all calculations for a relation
          return my_dict


     # interfact to processHistory
     def get_nonfitting_traces_from_traceMap(self) -> list:
          traces = []
          all_trace_ids = list(self.dataStructures.traceMap.keys())
          for id in all_trace_ids:
               if not self.__check_trace_alignment(id):
                    traces.append(id)
          return traces


     # private auxilary function 
     def __is_deviation(self, time, parameter) -> bool:
          
          avg = parameter[0]
          std = parameter[1]
          l = self.allowed_deviation
          upper_boundary = avg + (l * std)
          lower_boundary = avg - (l* std)
          if time >= lower_boundary and time <= upper_boundary:
               return True
          else:
               return False



     # for a given Trace and a given TimeModel
     def check_trace_alignment(self, trace_id) -> bool:

          time_spreads = self.__calc_time_spreads(trace_id)

          self.__update_time_model(time_spreads)

          outlier_counter = 0

          if self.active_time_model is not None:

               for relation in time_spreads:
                    # time kann auch eine Liste sein
                    time = time_spreads[relation]
                    parameter = self.active_time_model[relation]

                    if self.__is_deviation(time, parameter):
                         outlier_counter += 1 

               z = len(time_spreads)
               if z > 0: 
                    kpi = outlier_counter / len(time_spreads)
               else:
                    return False
               return kpi >= self.trace_Treshold
          else:
               return False


     # this function updates the time model if there are any unseen directly_follows relations
     #sollte das Time model hier immer mit dem neusten wert aus der unseen relation befüllt werden?
     def __update_time_model(self, time_spreads : dict) -> None:

          if self.active_time_model is None:
               #no update necassary
               return
          else:
               keys_time_model = set(self.active_time_model.keys())
               # get all the elements that are not in the time model
               remaining_relations = self.dataStructures.directly_follows_relations - keys_time_model
               if len(remaining_relations) == 0:
                    #das time model ist up to date
                    pass
               else:
                    # there are directly follows relations that the time model have not seen -> update
                    for new_relation in remaining_relations:
                         # hier nochmal wirklich schauen, ob die Logik hier so richtig ist
                         if len(time_spreads[new_relation]) > 1:
                              self.active_time_model[new_relation] = [statistics.mean(time_spreads[new_relation]), statistics.stdev(time_spreads[new_relation])]
                         else:
                              self.active_time_model[new_relation] = [statistics.mean(time_spreads[new_relation]), 0]

          
     
     # for a given Trace (mostly the active trace...)
     def __calc_time_spreads(self, trace_id) -> dict:

          trace = self.dataStructures.traceMap[trace_id]
          # dictionary to return
          time_spreads = dict()
          for x in range(0, len(trace)-1):
               first = trace[x]
               second = trace[x+1]
               time = abs(first.get_event_time() - second.get_event_time())

               if time_spreads.get((first.get_event_name(), second.get_event_name())) is not None:
                    #relation is already in the dictionary
                    time_spreads[(first.get_event_name(), second.get_event_name())].append(time.total_seconds())
               else:
                    time_spreads[(first.get_event_name(), second.get_event_name())] = [time.total_seconds()]
          
          return time_spreads


