from pybeamline.sources import log_source
from pybeamline.filters import excludes_activity_filter
from TraceMapHandler import TraceMapHandler

# this is the pipeline we will use as a "streaming engine"
# since we will implement an approach of the Process Histories all windowinf will be done within my_system
# ==> we will only need to process an event
# in the process new event function should be the API to my "System"

if __name__ == "__main__":

     my_traceMap = TraceMapHandler(10)


     log_source("synthData/recurring_time_noise0_100_baseline.xes").pipe(
    
    
     ).subscribe(lambda x: my_traceMap.process_new_event(x))

     print(str(my_traceMap.traceMap))
     print(str(my_traceMap.timeMap))
     print(str(my_traceMap.active_trace_ID))
     print(str(my_traceMap.directly_follows_relations))