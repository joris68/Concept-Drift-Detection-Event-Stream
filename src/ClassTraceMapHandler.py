from datetime import datetime

# this is the class for managing the Tracemap und the timestamps correlated to that

class TraceMapHandler:
     
     #holds python lists of Events for Traces
     traceMap = dict()

     # holds a tuple for every case. (timestamp first event entering the timemap, timestamp for last event of trace entering the traceMap)
     timeMap = dict()

     # defines the "sliding window"
     traceMapSize = 10

     # inserts simantaniously into thr tracemap and the timemap
     def process_new_event(cls, event) -> None:
         
          if cls.case_exists(event):   
              #insert event to existing case
              cls.traceMap[event.case].append(event)
              #update timeMap accordingly, 2. position in the tuple
              cls.timeMap[event.case][1] = datetime.now()

          else:
               if cls.enough_space():
                   cls.add_new_case(event)
               else:
                   cls.delete_oldest_trace()
                   cls.add_new_case(event)

                             

     # finds out the oldest trace, according to the first event inserted to the TraceMap? Maybe the latest? also makes sense -> not specified in the Paper
     def delete_oldest_trace(cls) -> None:

          #implementing linear search
          timestamp_now = datetime.now()
          largest_time_diff = 0
          case_to_be_deleted = None
          for key in cls.timeMap:
               diff = abs(cls.timeMap[key][0] - timestamp_now)
               if diff >= largest_time_diff:
                    largest_time_diff = diff
                    case_to_be_deleted = key

          try:

               del cls.traceMap[case_to_be_deleted]
               del cls.timeMap[case_to_be_deleted]

          except KeyError as e:

               print(f"KeyError, when deleting the oldest trace in the TraceMap and the Timemap {e}")


     def add_new_case(cls, event):
          cls.traceMap[event.case] = [event]
          cls.timeMap[event.case] = (datetime.now(), None)

     # boolean functions

     def case_exists(cls, event) -> bool:
          return event.case  in cls.traceMap.keys()  

     def enough_space(cls) -> bool:
          return len(cls.traceMap) <= cls.traceMapSize



if __name__ == "__main__":

     my_traceMap = TraceMapHandler.create_Trace_Map()
     print(my_traceMap)
