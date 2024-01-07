class Event:
    def __init__(self, case, event, timestamp):
        self.case = case
        self.event = event
        self.timestamp = timestamp
        
    def __str__(self) -> str:
        return f"{self.event}"