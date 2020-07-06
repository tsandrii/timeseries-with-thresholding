import pandas as pd
from fastai.tabular import add_datepart

"""
Data preparer function for ticker data to be used with an SMA method
"""


def ticker_sma(raw_data):
    x_features = pd.DataFrame({'x': [1] * len(raw_data['close'])})
    y_features = raw_data['close']
    return x_features, y_features


"""
Data preparer function for ticker data to be used with a Linear Regression (LR) method
"""


def ticker_lr(raw_data):
    x_features = pd.DataFrame({'x': [1] * len(raw_data['close'])})
    y_features = raw_data['close']
    return x_features, y_features


"""
Data preparer default function for ticker data
"""


def ticker_default(raw_data):
    x_features = pd.DataFrame({'x': list(range(0, len(raw_data['close'])))})
    y_features = raw_data['close']
    return x_features, y_features


"""
Data preparer function for ticker data to be used with an SVM method
"""


def ticker_svm(raw_data):
    data_copy = raw_data.copy()
    add_datepart(data_copy, 'date')
    data_copy.drop('Elapsed', axis=1, inplace=True)

    # setting importance of days before and after weekends
    # we assume that Fridays and Mondays are more important
    # 0 is Monday, 1 is Tuesday
    data_copy['mon_fri'] = 0
    data_copy['mon_fri'].mask(data_copy['Dayofweek'].isin([0, 4]), 1, inplace=True)
    data_copy['mon_fri'].where(data_copy['Dayofweek'].isin([0, 4]), 0, inplace=True)

    x_features = data_copy.drop('close', axis=1)
    y_features = data_copy['close']
    return x_features, y_features
