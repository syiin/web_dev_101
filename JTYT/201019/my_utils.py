import pandas as pd
import datetime
import numpy as np

def add_2_numbers(x, y):
    return x + y

def label_columns(ticker):
    df = pd.read_csv(f'data/Stocks/{ticker}.us.txt',
                     header=0, parse_dates=[0], date_parser=date_time_parser)
    df = df.rename(columns={"Open": f"Open_{ticker}",
                            "High": f"High_{ticker}",
                            "Low": f"Low_{ticker}",
                            "Close": f"Close_{ticker}",
                            "Volume": f"Volume_{ticker}"})
    return df

def date_time_parser(x):
    return datetime.datetime.strptime(x, '%Y-%m-%d')

def get_technical_indicators(dataset, counter_str):
    dataset['ma7'] = dataset[counter_str].rolling(window=7).mean()
    dataset['ma21'] = dataset[counter_str].rolling(window=21).mean()

    dataset['26ema'] = dataset[counter_str].ewm(span=26).mean()
    dataset['12ema'] = dataset[counter_str].ewm(span=12).mean()
    dataset['MACD'] = (dataset['12ema'] - dataset['26ema'])

    dataset['20sd'] = dataset[counter_str].rolling(20).std()
    dataset['upper_band'] = dataset['ma21'] + (dataset['20sd'] * 2)
    dataset['lower_band'] = dataset['ma21'] - (dataset['20sd'] * 2)

    dataset['ema'] = dataset[counter_str].ewm(com=0.5).mean()

    dataset['momentum'] = dataset[counter_str] - 1
    dataset['log_momentum'] = np.log(dataset['momentum'])
    return dataset
