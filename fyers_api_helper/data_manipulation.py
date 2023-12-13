from .config import get_app_id
from .access import get_access_token
from fyers_apiv3 import fyersModel
# from datetime import date
from datetime import timedelta
import pandas as pd
import time

APP_ID = get_app_id()
ACCESS_TOKEN = get_access_token()

fyers = fyersModel.FyersModel(
       client_id=APP_ID,
       token=ACCESS_TOKEN,
       log_path="")


def historical_bydate(symbol, start_date, end_date, resolution):
    data = {
          "symbol": symbol,
          "resolution": resolution,
          "date_format": "1",
          "range_from": start_date,
          "range_to": end_date,
          "cont_flag": "1"}
    try:
        return fyers.history(data)['candles']
    except Exception as e:
        print("Unable to collect data ...\n\n")
        return fyers.history(data)
        raise e


def get_data(fyers,
             symbol,
             start_date,
             end_date,
             resolution,
             in_timestamp=True,
             sleep=2):
    '''
    This function is used to get formatted data.
    fyers                       ->      fyersModel object
    start_date                  ->      datetime.date
    end_date                    ->      datetime.date
    resolution                  ->      string (same as in Fyers API doc)
    in_timestamp=True (default) ->      returns Date column in timestamp
    in_timestamp=False          ->      returns Date column in datetime
    sleep=2                     ->      Sleep after iteration (for API limit)
    '''

    start_date = start_date
    end_date = end_date
    df = pd.DataFrame()
    in_timestamp = False
    ed = start_date

    while start_date + timedelta(days=100) < end_date:
        ed = start_date + timedelta(days=99)

        dx = historical_bydate(
                symbol,
                start_date.strftime("%Y-%m-%d"),
                ed.strftime("%Y-%m-%d"),
                resolution)

        df = pd.concat([df, pd.DataFrame(dx)])
        start_date += timedelta(days=100)
        time.sleep(sleep)

    dx = historical_bydate(symbol,
                           start_date.strftime("%Y-%m-%d"),
                           end_date.strftime("%Y-%m-%d"),
                           resolution)

    df = pd.concat([df, pd.DataFrame(dx)])
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

    if not in_timestamp:
        df['Date'] = pd.to_datetime(df['Date'], unit='s')
        df['Date'] = df['Date'].dt.tz_localize('UTC')
        df['Date'] = df['Date'].dt.tz_convert('Asia/Kolkata')

    return df

# # Usage of get_data method
#
#
# start_data = date(2021, 1, 1)
# end_date = date(2022, 1, 1)
# df = get_data(fyers,
#               "NSE:NIFTY50-INDEX",
#               start_data,
#               end_date,
#               "1",
#               in_timestamp=False,
#               sleep=1)
#
# print(df)
# print(df.dtypes)
