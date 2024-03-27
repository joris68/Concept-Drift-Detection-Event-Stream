
class TimeModel:

     # deviation will be in standarddeviations from the average
     # the structure will be like this:
     # key will be a relation tuple from the directly follows map
     # value will be a list of lenght two : [average, std]
     # unit of both will be (milli)seconds.


     def __init__(self, times: dict) -> None:
          self.times = times

     def __str__(self):
        return '\n'.join([f"{key}: {value}" for key, value in self.times.items()])
          