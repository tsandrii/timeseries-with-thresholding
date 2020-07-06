import numpy as np

"""
Differentiates a time series to make it stationary
 - '1' (order 1): X(n) <- X(n) - X(n-1)
 - '2' (order 2): X(n) <- X(n) - 2 X(n-1) - X(n-2)
 - 'return-price': X(n) <- (X(n) - X(n-1)) / X(n-1)

Parameters:
    data (pd.DataFrame): Data with 'close' and 'date' columns
    order (str): Order of differentiation
        (default is 1)

Returns:
    data_diff (pd.DataFrame): DataFrame with a differentiated 'close' price column
"""


def differentiate(data, order='1'):
    diff_data = data.copy()
    if order == '0':
        return diff_data
    if order == '1':
        diff_data = data.diff().fillna(0)
    elif order == 'return-price':
        diff_data = (data.diff() / data.shift(periods=1)).fillna(0)
    else:
        diff_data = data.diff().fillna(0)
        diff_data.drop(diff_data.index[0], inplace=True)
        diff_data = differentiate(diff_data, str(int(order)-1))
    return diff_data


"""
Computes the inverse of differentiation on a time series. 
initial_val is required to rebuild the time series when order > 0
and corresponds to the first used value in the time series when 
treating the time series as chronological.

Parameters:
    predictions (list(float)): Predicted values given by a forecast
    diff_order (str): Order of differentiation, see differentiate() 
        for more info
    initial_val (float): Start value for time series

Returns:
    inv_diff_predictions (list(float)): recreated time series of predictions
        from differentiated values
"""


def inv_differentiate(predictions, order, initial_val):
    if order == '0':
        return np.array(predictions)
    elif order == '1':
        inv_diff_predictions = [initial_val + predictions[0]]

        for i in range(len(predictions)-1):
            inv_diff_predictions.append(predictions[i+1] + inv_diff_predictions[i])

        return np.array(inv_diff_predictions)
    elif order == 'return-price':
        inv_diff_predictions = [predictions[0] * initial_val + initial_val]

        for i in range(len(predictions)-1):
            inv_diff_predictions.append(predictions[i+1] * inv_diff_predictions[i] + inv_diff_predictions[i])

        return np.array(inv_diff_predictions)


"""
Applies min-max normalization to get in a specific range. Useful
for visualization purposes of returns vs. close price comparisons
"""


def min_max_normalize(data):
    return (data - min(data)) / (max(data) - min(data))


""" 
Checks x and y data to make sure the length matches, and if x_data
provided is None, generates a monotonically increasing series from 0 to n
to use as the x series while the y series is what is being predicted
"""


def generate_and_verify_data(x_data, y_data):
    if x_data is None:
        x_data = list(range(0, len(y_data)))
    assert len(x_data) == len(y_data)
    return x_data, y_data


"""
Gets the correct amount of training data from a data list based on a time
t requested and the look back. Useful for avoiding out-of-bounds errors
"""


def training_data_for_t(data, t, look_back):
    x_data, y_data = generate_and_verify_data(x_data=data[0], y_data=data[1])
    assert len(x_data) == len(y_data)

    if look_back == -1 or t < look_back:
        x_train, y_train = x_data[:t], y_data[:t]
    else:
        x_train, y_train = x_data[t - look_back:t + 1], y_data[t - look_back:t + 1]
    return x_train, y_train


"""
Returns whether a percent change between two values is above a specified threshold.
Useful for making decisions based on thresholds
"""


def change_above_threshold(first, second, threshold):
    change = (abs(second - first) / first) * 100.0
    if change >= threshold:
        return True
    return False
