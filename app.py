from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, user: {{ tower_user_name }} host: {{ ansible_hostname }} !</p>"

