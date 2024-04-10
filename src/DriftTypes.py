from enum import Enum


class DriftType(Enum):
    """These are all possible Drift Types."""

    SUDDEN = "Sudden Drift"
    RECURRING = "Recurring Drift"  # kanns den überhaut geben alleine geben?
    INCREMENTAL = "Incremental Drift"
    GRADUAL = "Gradual Drift"
    SUDDEN_RECURRING = "Sudden Recurring"
    INCREMENTAL_RECURRING = "Incremental Recurring"
