
from Event import Event
from TraceMapHandler import TraceMapHandler
from datetime import datetime

if __name__ == "__main__":

     # generate three Events

     e1 = Event(1, "A", datetime.now())
     e2 = Event(2, "B", datetime.now())
     e3 = Event(3, "C", datetime.now())

     a = []
     a.append(e1)
     a.append(e2)
     a.append(e3)


     for e in a:
          TraceMapHandler.process_new_event(event=e)
          print(str(TraceMapHandler.active_trace_ID))
     
     print(str(TraceMapHandler.traceMap))
     print(str(TraceMapHandler.timeMap))