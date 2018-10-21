from time import time


class TimeMeasuring:

    def __init__(self):
        pass

    @staticmethod
    def print_fit_time(start_time):
        print "Fit time: ", time() - start_time, "s"

    @staticmethod
    def print_prediction_time(start_time):
        print "Prediction time: ", time() - start_time, "s"