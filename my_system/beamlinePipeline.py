from pybeamline.sources import log_source
from pybeamline.filters import excludes_activity_filter
from TraceMapHandlerBEvent import TraceMapHandlerBEvent

# this is the pipeline we will use as a "streaming engine"
# since we will implement an approach of the Process Histories all windowinf will be done within my_system
# ==> we will only need to process an event


log_source("synthData/recurring_time_noise0_100_baseline.xes").pipe(
    
    
).subscribe(lambda x: TraceMapHandlerBEvent.process_new_event(x))

print(str(TraceMapHandlerBEvent.traceMap))
print(str(TraceMapHandlerBEvent.timeMap))
print(str(TraceMapHandlerBEvent.active_trace_ID))