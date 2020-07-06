from methods import Method
from utils.general import training_data_for_t

"""
Simple Moving Average (SMA) prediction model / method
"""


class MovingAverage(Method):
    def predict(self, t, x_data, y_data, look_back=-1):
        # -1 means look back at as much data as possible
        # get the training data slice for the current t
        _, y_train = training_data_for_t(data=(x_data, y_data), t=t, look_back=look_back)
        return y_train.sum() / len(y_train)

    def predict_next_n(self, t, n, x_data, y_data, look_back=-1):
        # -1 means look back at as much data as possible
        predictions = []

        # forecast for N periods
        for i in range(n):
            t_i = t + i
            # get the training data slice for the current t_i
            _, y_train = training_data_for_t(data=(x_data, y_data), t=t_i, look_back=look_back)

            moving_average = y_train.sum() / len(y_train)
            predictions.append(moving_average)

        assert len(predictions) == n
        return predictions
