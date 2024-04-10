from datetime import datetime
import logging


class TraceMapHandler:
    """
    This is the class for managing the Tracemap und the timestamps correlated to that. It performs the windowing mechanism of the string.
    It also monitors the the directly-follows relations in the process.
    """

    def __init__(self, traceMapSize) -> None:
        # holds python lists of Events for Traces
        self.traceMap = dict()
        # holds a list for every case. [timestamp first event entering the traceMap, timestamp for last event of trace entering the traceMap]
        self.timeMap = dict()
        # defines the "sliding window"
        self.traceMapSize = traceMapSize
        # holds the case ID of the currently processed Event for easy access for further analysis
        self.active_trace_ID = None
        # manages the directly follows relations for building our time model
        self.directly_follows_relations = set()
        self.processed_events = 0

    # inserts simantaniously into the tracemap and the timemap, also manages
    def process_new_event(self, event) -> None:

        self.active_trace_ID = event.get_trace_name()
        # logging.info(f"Active Trace: {self.active_trace_ID} Handling the event rigth now")

        if self.__case_exists(event):
            self.traceMap[event.get_trace_name()].append(event)
            # update timeMap accordingly, 2. position in the list
            self.timeMap[event.get_trace_name()][1] = datetime.now()
            # ogging.info(f"Inserted new Event in already existing Trace in the Maps")

        else:
            if self.__enough_space():
                self.__add_new_case(event)
            else:
                self.__delete_oldest_trace()
                self.__add_new_case(event)

        # manage the DF relations regardlessly
        self.__manage_df_relations()
        self.processed_events += 1
        #logging.info("Processes event accordingly")

    # finds out the oldest trace, according to the first event inserted to the TraceMap? Maybe the latest? also makes sense -> not specified in the Paper
    def __delete_oldest_trace(self) -> None:

        # implementing linear search
        timestamp_now = datetime.now()
        largest_time_diff = 0
        case_to_be_deleted = None
        for key in self.timeMap:
            diff = abs(self.timeMap[key][0] - timestamp_now)
            if diff.total_seconds() >= largest_time_diff:
                largest_time_diff = diff.total_seconds()
                case_to_be_deleted = key

        try:

            del self.traceMap[case_to_be_deleted]
            del self.timeMap[case_to_be_deleted]
            # logging.info(f"Trace with Key {case_to_be_deleted} got deleted")

        except KeyError as e:

            print(
                f"KeyError, when deleting the oldest trace in the TraceMap and the Timemap {e}"
            )

    def __add_new_case(self, event):
        self.traceMap[event.get_trace_name()] = [event]
        self.timeMap[event.get_trace_name()] = [datetime.now(), None]
        # logging.info(f"New trace with traceID {event.get_trace_name()} got inserted into the Tracemap and the TimeMap")

    # boolean functions

    def __case_exists(self, event) -> bool:
        return event.get_trace_name() in self.traceMap.keys()

    def __enough_space(self) -> bool:
        return len(self.traceMap) <= self.traceMapSize

    def __manage_df_relations(self) -> None:
        # takes active trace and checks for a new directly follows relations
        a_trace = self.traceMap[self.active_trace_ID]
        length = len(a_trace)
        if length == 1:
            pass
        else:
            # the the penultimate and ulitmate  Element from the trace (in this order!!) and check the directly_follows set if it
            # contains this relationship (penultimate, ultimate)
            new_tuple = (
                a_trace[len(a_trace) - 2].get_event_name(),
                a_trace[len(a_trace) - 1].get_event_name(),
            )

            if new_tuple in self.directly_follows_relations:
                pass
                # logging.info(f"Already existing directly follows relationship")
            else:
                self.directly_follows_relations.add(new_tuple)
                # logging.info(f"We found a new directly follows relation {new_tuple} and added it to the Set")
