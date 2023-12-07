from flask import Flask, request, render_template
from waitress import serve
import webbrowser
import json

app = Flask(__name__)
app.secret_key = 'SAMPLE SECRET'

app_id = ''
secret_id = ''
redirect_url = ''


@app.route('/', methods=['GET', 'POST'])
def index():
    global app_id, secret_id, redirect_url
    if request.method == 'POST':
        app_id = request.form['app_id']
        secret_id = request.form['secret_id']
        redirect_url = request.form['redirect_url']
        save()
        print("Information Saved Successfully .. Press Ctrl-C to continue")
        return "Information Saved Successfully"
    return render_template('config.html')


def save():
    data = {
            'APP_ID': app_id,
            'SECRET_ID': secret_id,
            'REDIRECT_URL': redirect_url
            }
    with open('data/config.json', 'w') as f:
        json.dump(data, f)


def get_app_id():
    with open('data/config.json', 'r') as f:
        data = json.load(f)
    return data["APP_ID"]


def get_secret_id():
    with open('data/config.json', 'r') as f:
        data = json.load(f)
    return data["SECRET_ID"]


def get_redirect_url():
    with open('data/config.json', 'r') as f:
        data = json.load(f)
    return data["REDIRECT_URL"]


def set_config():
    webbrowser.open_new('http://localhost:7001')
    serve(app, host='0.0.0.0', port=7001)


if __name__ == "__main__":
    set_config()
