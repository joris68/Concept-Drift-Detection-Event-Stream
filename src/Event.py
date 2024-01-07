class Event:
    def __init__(self, case, activity , timestamp):
        self.case = case
        self.event = activity
        self.timestamp = timestamp
        
    def __str__(self) -> str:
        return f"{self.event}"