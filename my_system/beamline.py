from pybeamline.sources import log_source
from pybeamline.filters import excludes_activity_filter
from TraceMapHandler import TraceMapHandler

log_source("synthData/recurring_time_noise0_100_baseline.xes").pipe(
    
    map(lambda x: BEvent())
    
).subscribe(lambda x: TraceMapHandler.process_new_event(x))