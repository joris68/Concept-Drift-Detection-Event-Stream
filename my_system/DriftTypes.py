from enum import Enum

class DriftType(Enum):
    VALUE1 = "Sudden Drift"
    VALUE2 = "Recurring Drift"
    VALUE3 = "Incremental Drift"
    VALUE4 = "Gradual Drift"