from flask import Flask, request, render_template
from waitress import serve
import webbrowser
import json
import os

app = Flask(__name__)
app.secret_key = 'SAMPLE SECRET'

app_id = ''
secret_id = ''
redirect_url = ''

CONFIG_FILE_PATH = os.path.join(os.path.expanduser("~"), ".fyers_config.json")


class FyersAPIHelper(Exception):
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    global app_id, secret_id, redirect_url
    if request.method == 'POST':
        app_id = request.form['app_id']
        secret_id = request.form['secret_id']
        redirect_url = request.form['redirect_url']
        save_config()
        print("Information Saved Successfully .. Press Ctrl-C to continue")
        return "Information Saved Successfully"
    return render_template('config.html')


def save_config():
    data = {
            'APP_ID': app_id,
            'SECRET_ID': secret_id,
            'REDIRECT_URL': redirect_url
            }
    set_data(data)


def load_config():
    # I have no idea why this works with try catch block only.
    try:
        with open(CONFIG_FILE_PATH, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {
            'APP_ID': '',
            'SECRET_ID': '',
            'REDIRECT_URL': ''
            }
        set_data(data)
        with open(CONFIG_FILE_PATH, 'r') as f:
            data = json.load(f)
    return data


def get_app_id():
    data = load_config()
    return data["APP_ID"]


def get_secret_id():
    data = load_config()
    return data["SECRET_ID"]


def get_redirect_url():
    data = load_config()
    return data["REDIRECT_URL"]


def set_config():
    webbrowser.open_new('http://localhost:7001')
    serve(app, host='127.0.0.1', port=7001)


def set_config_manually(option, value):
    data = load_config()
    data[option] = value
    set_data(data)


def set_data(data):
    with open(CONFIG_FILE_PATH, 'w+') as f:
        json.dump(data, f)


def print_config():
    try:
        data = load_config()
        print(f'''
APP ID:         {data["APP_ID"]}
SECRET ID:      {data["SECRET_ID"]}
REDIRECT URL:   {data["REDIRECT_URL"]}
            ''')
    except Exception:
        print('Configuration not found. Please set up configuration first.')
        exit(1)


if __name__ == "__main__":
    set_config()
