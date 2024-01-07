

# we will implement this with the singleton pattern

class TraceMap:
    _instance = None
    
    # Constructor to enforce Singleton
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.size = kwargs.get('size', 10)
            cls._instance.traceMap = cls._instance.create_buckets(cls._instance.size)
            cls._instance.timeMap = cls._instance.create_tuples(cls._instance.size)
        return cls._instance

    def create_buckets(self, size):
        return [[] for _ in range(size)]

    def create_tuples(self, size):
        return [() for _ in range(size)]


if __name__ == "__main__":

     my_traceMap =TraceMap(size = 5)
     my_2traceMap = TraceMap(size = 6)
     print(my_traceMap)
     print(my_2traceMap)