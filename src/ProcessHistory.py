from ModelHandler import ModelHandler
from TraceMapHandler import TraceMapHandler
from pybeamline.sources import log_source
from DriftTypes import DriftType
import logging
import pprint
import math
import statistics


class ProcessHistory:
    """
    This class orchestrates ths tasks from the Modelhandler and the tracemaphandler, also it has the logic for the
    concept drift distinction.
    """

    def __init__(
        self,
        modelHandler: ModelHandler,
        lower_boundary: int,
        anomaly_treshhold: float,
        cohens_boundary,
        model_epsilon,
    ) -> None:
        self.modelHandler = modelHandler
        self.processHistory = []
        self.events_lower_boundary = lower_boundary
        # brauch ich das wirklich hier?
        self.anomaly_treshhold = anomaly_treshhold
        self.cohens_boundary = cohens_boundary
        self.model_epsilon = model_epsilon

    def concept_Drift_detection(self, event):

        self.modelHandler.dataStructures.process_new_event(event)
        # isAlining = self.modelHandler.check_trace_alignment(self.modelHandler.dataStructures.active_trace_ID, self.modelHandler.active_time_model)

        if len(self.processHistory) > 0:

            isAlining = self.modelHandler.check_trace_alignment(
                self.modelHandler.dataStructures.active_trace_ID,
                self.modelHandler.active_time_model,
            )
            logging.info(f"active trace will be conformanced checked : {isAlining}")
            if not isAlining:

                potential_new_model = self.modelHandler.mine_new_model(
                    self.modelHandler.get_nonfitting_traces_from_traceMap()
                )

                if self.modelHandler.calculate_model_score(
                    potential_new_model, self.anomaly_treshhold
                ):
                    self.processHistory.append(potential_new_model)
                    self.modelHandler.active_time_model = self.processHistory[-1]
                    pprint.pprint(self.modelHandler.active_time_model.times)
                    print()
                    logging.info(
                        "new Model got appended to the process History, and is now active."
                    )
                    self.concept_drift_distinction()

        elif len(self.processHistory) == 0:

            if (
                self.modelHandler.dataStructures.processed_events
                >= self.events_lower_boundary
            ):
                # mine initial model
                initial_timemodel = self.modelHandler.mine_new_model(trace_ids=None)
                logging.info("Initial timemodel was mined")
                self.processHistory.append(initial_timemodel)
                self.modelHandler.active_time_model = self.processHistory[-1]
                print("Initial Timemodel was found")
                pprint.pprint(initial_timemodel.times)
                print()
                logging.info(
                    "Initial timemodel was appended to the history, and is now active"
                )

    def concept_drift_distinction(self) -> DriftType:
        if len(self.processHistory) <= 1:
            raise Exception("How come we make distinctions?")

        if len(self.processHistory) == 2:
            # just calculate the cohens d ==> possible outcomes: incremental and sudden drift
            score = self.calculate_cohens(
                self.processHistory[-2], self.processHistory[-1]
            )
            type = self.categorize_cohens(score)
            print(f"Detected: {str(type)} with score {str(score)}")

        if len(self.processHistory) >= 3:
            # hier müssen wir auch nach recurrig drifts checken
            # für jedes model in der history den Modelscore berechnen und gucken ob es einen recurring drift gibt
            # outcome kann hier sein, recurring sudden, oder recurring incremental
            # ode einfach nur sudden oder nur incremental
            model_scores = []
            for model in self.processHistory:
                score = self.modelHandler.calculate_model_score(
                    model, self.anomaly_treshhold
                )
                model_scores.append(score)

            # check for recurring drift
            is_recurring = self.check_score_difference(model_scores, self.model_epsilon)
            # calculate cohen's d between the the ultimate and penultimate timemodel
            cohens = self.calculate_cohens(
                self.processHistory[-2], self.processHistory[-1]
            )
            change_drift = self.categorize_cohens(cohens)

            if is_recurring:
                if change_drift == DriftType.SUDDEN:
                    print(
                        f"Detected: {str(DriftType.SUDDEN_RECURRING)} with score {str(cohens)}"
                    )
                if change_drift == DriftType.INCREMENTAL:
                    print(
                        f"Detected: {str(DriftType.INCREMENTAL_RECURRING)} with score {str(cohens)}"
                    )
            else:
                print(f"Detected: {str(change_drift)} with score {cohens}")

    def categorize_cohens(self, cohens_score):
        if cohens_score >= self.cohens_boundary:
            return DriftType.SUDDEN
        else:
            return DriftType.INCREMENTAL

    def check_score_difference(self, model_scores, epsilon):
        for i in range(len(model_scores)):
            for j in range(i + 1, len(model_scores)):
                if abs(model_scores[i] - model_scores[j]) < epsilon:
                    return True
        return False

    # this function takes cohen's d measurement and maps it onto the timemodel
    def calculate_cohens(self, timemodel1, timemodel2):
        ds = []
        # assuming same lenght
        for rel, values in timemodel1.times.items():
            av1 = values[0]
            av2 = timemodel2.times[rel][0]
            std1 = values[1]
            # std kann null sein, dann müssen wir skippen
            if std1 == 0.0:
                continue
            std2 = timemodel2.times[rel][1]
            if std1 == 0.0:
                continue
            oben = av1 + av2
            sample_size = (
                self.modelHandler.dataStructures.traceMapSize * self.anomaly_treshhold
            )
            unten = math.sqrt(
                (sample_size * std1**2 + sample_size * std2**2) / (2 * sample_size - 2)
            )
            ds.append(oben / unten)

        return statistics.mean(ds)
