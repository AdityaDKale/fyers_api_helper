from .config import get_app_id, get_secret_id, get_redirect_url
from flask import Flask, request, render_template
from waitress import serve
import webbrowser
import json
from datetime import datetime
from fyers_apiv3 import fyersModel
import threading
import os

today = datetime.today()

ACCESS_FILE_PATH = os.path.join(os.path.expanduser("~"), ".fyers_access.json")

app = Flask(__name__)
app.secret_key = 'SAMPLE SECRET'

access_token = ''
auth_code = ''
appSession = None

try:
    APP_ID = get_app_id()
    SECRET_KEY = get_secret_id()
    REDIRECT_URL = get_redirect_url()
except Exception:
    APP_ID = ""
    SECRET_KEY = ""
    REDIRECT_URL = ""


def get_access(silent=False):
    global APP_ID, REDIRECT_URL, SECRET_KEY, appSession
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
    if not silent:
        webbrowser.open(generateTokenUrl, new=1)
    else:
        print(generateTokenUrl)


class FyersAPIHelper(Exception):
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    global access_token, today, auth_code, appSession
    auth_code = request.args.get('auth_code', '')
    if request.method == 'POST':
        auth_code = request.form['auth_code']
        today = request.form['date']
        appSession.set_token(auth_code)
        response = appSession.generate_token()
        access_token = response['access_token']
        save_access()
        print("Access Token saved Successfully .. Press Ctrl-C to continue")
        return "Access Token saved Successfully"
    return render_template(
            'access.html',
            auth_code=auth_code,
            today=today.strftime('%d-%m-%Y'))


def save_access():
    data = {
            'ACCESS_TOKEN': access_token,
            'DATE': today,
            }
    set_data(data)


def load_access():
    try:
        with open(ACCESS_FILE_PATH, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {
            'ACCESS_TOKEN': '',
            'DATE': '',
            }
        set_data(data)
        with open(ACCESS_FILE_PATH, 'r') as f:
            data = json.load(f)
    return data


def set_access():
    serve(app, host='127.0.0.1', port=7000)


def set_access_manually(option, value):
    data = load_access()
    data[option] = value
    set_data(data)


def set_data(data):
    with open(ACCESS_FILE_PATH, 'w+') as f:
        json.dump(data, f)


def print_access():
    data = load_access()
    print(f'''
ACCESS TOKEN:   {data["ACCESS_TOKEN"]}
DATE:           {data["DATE"]}
          ''')


def check_valid(data, silent=True):
    if data["DATE"] == today.strftime('%d-%m-%Y'):
        if not silent:
            print("Access Token Valid")
        return True
    else:
        if not silent:
            print("Access Token Invalid")
        return False


def get_access_token():
    data = load_access()
    valid = check_valid(data)
    return data["ACCESS_TOKEN"] if valid else None


def run():
    thread_get_access_token = threading.Thread(target=get_access)
    thread_get_access_token.start()
    set_access()


if __name__ == "__main__":
    run()
