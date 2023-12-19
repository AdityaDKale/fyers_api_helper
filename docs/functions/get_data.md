## Get Data

The ```get_data()``` function as the name suggests is used to get historical candlestick data from Fyers API but has no limitations on how much data can be retrieved from it.

!> Please use this function carefully and respect the Fyers API [limits](https://myapi.fyers.in/docsv3#tag/Request-and-Response-Structure/paths/~1pet~1%7BpetId%7D/get). You can use the sleep attribute of get data method to lower down the speed of API Calls.

```python
get_data(fyers, symbol, start_date, end_date, resolution, in_timestamp=True, sleep=2)
```


| Attribute                    	| Type                                      |
|-----------------------------	|---------------------------------------	|
| fyers                         | fyersModel object                         |
| start_date                  	| datetime.date                         	|
| end_date                    	| datetime.date                         	|
| resolution                  	| string (same as in Fyers API [docs](https://myapi.fyers.in/docsv3#tag/Data-Api/paths/~1DataApi/post))     	|
| in_timestamp=True (default) 	| returns Date column in timestamp      	|
| in_timestamp=False          	| returns Date column in datetime       	|
| sleep=2                     	| Sleep after iteration (for API limit) 	|


### Example

```python
from fyers_apiv3 import fyersModel
from fyers_api_helper import get_app_id, get_access_token, get_data
from datetime import date

client_id = get_app_id()
access_token = get_access_token()

fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")


start_data = date(2021, 1, 1)
end_date = date(2022, 1, 1)
df = get_data(fyers,
              "NSE:NIFTY50-INDEX",
              start_data,
              end_date,
              "1",
              in_timestamp=False,
              sleep=1)

print(df)
```

Output

```bash
$ python data.py 
                           Date      Open  ...     Close  Volume
0     2021-01-01 09:15:00+05:30  13997.90  ...  14014.85       0
1     2021-01-01 09:16:00+05:30  14013.85  ...  14008.05       0
2     2021-01-01 09:17:00+05:30  14007.15  ...  14013.65       0
3     2021-01-01 09:18:00+05:30  14013.75  ...  14015.45       0
4     2021-01-01 09:19:00+05:30  14016.30  ...  14016.00       0
...                         ...       ...  ...       ...     ...
92477 2021-12-31 15:25:00+05:30  17357.90  ...  17356.30       0
92478 2021-12-31 15:26:00+05:30  17356.10  ...  17359.25       0
92479 2021-12-31 15:27:00+05:30  17358.85  ...  17359.80       0
92480 2021-12-31 15:28:00+05:30  17359.75  ...  17353.55       0
92481 2021-12-31 15:29:00+05:30  17353.45  ...  17364.25       0

[92482 rows x 6 columns]
```
