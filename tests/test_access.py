from fyers_api_helper import get_access_token, get_app_id
from fyers_apiv3 import fyersModel


def test_get_access_token():
    client_id = get_app_id()
    access_token = get_access_token()
    fyers = fyersModel.FyersModel(
            client_id=client_id,
            is_async=False,
            token=access_token,
            log_path="")
    response = fyers.get_profile()
    print(response)
    assert response['code'] == 200
