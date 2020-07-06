import matplotlib.pyplot as plt
from utils.general import min_max_normalize

"""
Plots a visualization of time series forecast values vs. the
ground truth
"""


def plot_forecast(forecast_data, true_data):
    xs = list(range(0, len(forecast_data)))  # create an x axis

    plt.plot(xs, forecast_data, c='b', label='predicted')
    plt.plot(xs, true_data, c='r', label='true')

    plt.legend(loc='upper left')
    plt.show()


"""
Plots a visualization of balance over time after completion of a
a series of trades simulation
"""


def plot_balance(data):
    xs = list(range(0, len(data)))  # create an x axis

    plt.plot(xs, data, c='green', label='Balance')

    plt.title("balance over time")
    plt.legend(loc='upper left')
    plt.show()


"""
Plots a visualization of balance vs. true values over time. Each time 
series is normalized to [0, 1] for comparison purposes
"""


def plot_balance_vs_price(balances, price, title):
    xs = list(range(0, len(balances)))  # create an x axis

    normalized_balances = min_max_normalize(balances)
    normalized_price = min_max_normalize(price)

    plt.plot(xs, normalized_balances, c='green', label='Balance')
    plt.plot(xs, normalized_price, c='black', label='Price')

    plt.title(title)
    plt.legend(loc='upper left')
    plt.show()


"""
Plots two time series side-by-side
"""


def plot_time_series(ts_1, ts_label_1, ts_2, ts_label_2, title):
    assert len(ts_1) == len(ts_2)
    xs = list(range(0, len(ts_1)))

    plt.plot(xs, ts_1, c='green', label=ts_label_1)
    plt.plot(xs, ts_2, c='red', label=ts_label_2)

    plt.title(title)
    plt.legend(loc='upper left')
    plt.show()


"""
Plots time series along with the forecast overlapped
"""


def plot_time_series_with_forecast(time_series, forecast):
    xs = list(range(0, len(time_series)))

    num_no_forecast = (len(time_series) - len(forecast))
    zeroed_forecast = [None] * num_no_forecast
    zeroed_forecast.extend(forecast)

    plt.plot(xs, time_series, c='green', label='Original')
    plt.plot(xs, zeroed_forecast, c='red', label='Forecast from t={}'.format(num_no_forecast))

    plt.title('forecast for {} points into future from t={}'.format(len(forecast), len(time_series) - len(forecast)))
    plt.legend(loc='upper left')
    plt.show()
