import requests
import pandas as pd
from io import StringIO

from utils.config import ALPHAVANTAGE_API_KEY


def check_limits(data):
    if '"Note": "Thank you for using Alpha Vantage!' in str(data):
        raise RuntimeError('API limit reached')


"""
Constructs a desired TIME_SERIES_INTRADAY AlphaVantage API URL

Parameters:
    symbol (str): Stock ticker symbol
    api_key (str): API key provided by AlphaVantage
    interval (str): Frequency of time series
        (default is '5min')

Returns:
    (str): AlphaVantage URL
"""


def generate_intraday_url(symbol, api_key, interval='5min'):
    base_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY'
    base_url += '&symbol={}'.format(symbol)
    base_url += '&interval={}'.format(interval)
    base_url += '&apikey={}'.format(api_key)
    base_url += '&datatype=csv'
    base_url += '&outputsize=full'
    return base_url


"""
Create and return a pd.DataFrame containing the date and close price fields for 
a stock ticker time-series via AlphaVantage. If available, retrieve from disk,
otherwise option to download via the API. 

Parameters:
    symbol (str): Stock ticker symbol
    interval (str): Frequency of the time series requested via the API
        (default is '5min')
    download (bool): Specifies whether to retrieve the data from disk or download
        (default is False)

Returns:
    data (pd.DataFrame): Data with a 'date' and 'close' column ordered chronologically
"""


def get_ticker_data(symbol, interval='5min', download=False):
    if download:
        response = requests.get(generate_intraday_url(symbol=symbol, interval=interval, api_key=ALPHAVANTAGE_API_KEY)).content
        check_limits(response)
        df = pd.read_csv(StringIO(response.decode('utf-8')))
    else:
        if interval == 'daily':
            df = pd.read_csv('data/daily/daily_{}.csv'.format(symbol))
        else:
            df = pd.read_csv('{}.csv'.format(symbol))

    cols = ['timestamp', 'close']
    df[cols[0]] = pd.to_datetime(df[cols[0]], format='%Y-%m-%d')
    df.index = df[cols[0]]
    df = df.sort_index(ascending=True, axis=0)

    data = pd.DataFrame(index=range(0, len(df)), columns=['date', 'close'])
    data['date'] = df[cols[0]].values
    data['close'] = df[cols[1]].values
    return data
