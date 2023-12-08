from flask import Flask, request, render_template
from .config import get_app_id, get_secret_id, get_redirect_url
from waitress import serve
import webbrowser
import json
from datetime import datetime
from fyers_apiv3 import fyersModel
import threading

today = datetime.today()

app = Flask(__name__)
app.secret_key = 'SAMPLE SECRET'

access_token = ''
APP_ID = get_app_id()
SECRET_KEY = get_secret_id()
REDIRECT_URL = get_redirect_url()


def get_access_token():
    global APP_ID, REDIRECT_URL, SECRET_KEY
    grant_type = 'authorization_code'
    response_type = 'code'
    state = 'sample'
    appSession = fyersModel.SessionModel(
            client_id=APP_ID,
            redirect_uri=REDIRECT_URL,
            secret_key=SECRET_KEY,
            response_type=response_type,
            state=state,
            grant_type=grant_type)
    generateTokenUrl = appSession.generate_authcode()
    webbrowser.open(generateTokenUrl, new=1)


class FyersAPIHelper(Exception):
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    global access_token, today
    auth_code = request.args.get('auth_code', '')
    if request.method == 'POST':
        access_token = request.form['access_token']
        today = request.form['date']
        save_access()
        print("Access Token saved Successfully .. Press Ctrl-C to continue")
        return "Access Token saved Successfully"
    return render_template(
            'access.html',
            auth_code=auth_code,
            today=today.strftime('%Y-%m-%d'))


def save_access():
    data = {
            'ACCESS_TOKEN': access_token,
            'DATE': today,
            }
    set_data(data)


def load_access():
    try:
        with open('.access.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FyersAPIHelper(
                'Access Token Not Found. Please Generate a new Token.')
    return data


def set_access():
    serve(app, host='127.0.0.1', port=7000)


def set_access_manually(option, value):
    data = load_access()
    data[option] = value
    set_data(data)


def set_data(data):
    with open('.access.json', 'w') as f:
        json.dump(data, f)


def print_access():
    data = load_access()
    print(f'''
ACCESS TOKEN:   {data["ACCESS_TOKEN"]}
DATE:           {data["DATE"]}
          ''')


def run():
    thread_get_access_token = threading.Thread(target=get_access_token)
    thread_get_access_token.start()
    set_access()


if __name__ == "__main__":
    run()
