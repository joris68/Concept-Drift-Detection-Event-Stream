from datetime import datetime

# this is the class for managing the Tracemap und the timestamps correlated to that
# everything except the Class variables and the process_new_event function will be considered strictly private.
# in this project private function are denoted with two underscore at the beginning of the name

class TraceMapHandlerBEvent:
     
     #holds python lists of Events for Traces
     traceMap = dict()

     # holds a tuple for every case. (timestamp first event entering the traceMap, timestamp for last event of trace entering the traceMap)
     timeMap = dict()

     # defines the "sliding window"
     traceMapSize = 10

     # holds the case ID of the currently processed Event for easy access for further analysis
     active_trace_ID = None

     # inserts simantaniously into the tracemap and the timemap
     @classmethod
     def process_new_event(cls, event) -> None:

          cls.active_trace_ID = event.get_trace_name()
         
          if cls.__case_exists(event):   
              #insert event to existing case
              cls.traceMap[event.get_trace_name()].append(event)
              #update timeMap accordingly, 2. position in the tuple
              cls.timeMap[event.get_trace_name()][1] = datetime.now()

          else:
               if cls.__enough_space():
                   cls.__add_new_case(event)
               else:
                   cls.__delete_oldest_trace()
                   cls.__add_new_case(event)

                             

     # finds out the oldest trace, according to the first event inserted to the TraceMap? Maybe the latest? also makes sense -> not specified in the Paper
     @classmethod
     def __delete_oldest_trace(cls) -> None:

          #implementing linear search
          timestamp_now = datetime.now()
          # will be measured in seconds
          largest_time_diff = 0
          case_to_be_deleted = None
          for key in cls.timeMap:
               diff = abs(cls.timeMap[key][0] - timestamp_now)
               if diff.total_seconds() >= largest_time_diff:
                    largest_time_diff = diff.total_seconds()
                    case_to_be_deleted = key

          try:

               del cls.traceMap[case_to_be_deleted]
               del cls.timeMap[case_to_be_deleted]

          except KeyError as e:

               print(f"KeyError, when deleting the oldest trace in the TraceMap and the Timemap {e}")

     @classmethod
     def __add_new_case(cls, event):
          cls.traceMap[event.get_trace_name()] = [event]
          cls.timeMap[event.get_trace_name()] = [datetime.now(), None]

     # boolean functions
     @classmethod
     def __case_exists(cls, event) -> bool:
          return event.get_trace_name()  in cls.traceMap.keys()  
     @classmethod
     def __enough_space(cls) -> bool:
          return len(cls.traceMap) <= cls.traceMapSize


