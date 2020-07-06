from utils.general import differentiate, inv_differentiate
import pandas as pd

"""
Given a method, data comprising the data points along the "x axis" and "y axis", and a starting point
in time, makes predictions for every data point into the future using the data for training.

Additionally, diff_order controls the differentiation order, and look_back controls the default
amount of time steps that the specific method uses to "look back" and train on.
"""


def forecast(method, data, start_t, look_back, diff_order='1'):
    x_features, y_features = data[0], data[1]
    assert len(x_features) == len(y_features)

    y_features_diff = differentiate(y_features, order=diff_order)
    predictions = []

    for t_i in range(len(y_features) - start_t):
        current_t = start_t + t_i
        predictions.append(method.predict(x_data=x_features, y_data=y_features_diff, t=current_t, look_back=look_back))

    inv_predictions = inv_differentiate(predictions, order=diff_order, initial_val=y_features[start_t - 1]).flatten()

    result = y_features[:start_t].append(pd.Series(inv_predictions)).reset_index(drop=True)
    return result.to_numpy()


"""
Variant of the base forecast() function, but allows to forecast N data points at once
starting from a time point start_t, where:
    N = (length of data passed in) - start_t
"""


def forecast_from_t(method, data, start_t, look_back, diff_order='1'):
    x_features, y_features = data[0], data[1]
    y_features_diff = differentiate(y_features, order=diff_order)
    num_predictions = (len(y_features_diff) - start_t)
    predictions = method.predict_next_n(x_data=x_features, y_data=y_features_diff, t=start_t, n=num_predictions, look_back=look_back)
    return inv_differentiate(predictions, order=diff_order, initial_val=y_features[start_t - 1])
