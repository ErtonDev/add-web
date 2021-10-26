from flask import Flask
from psqlapi import connect, post, get, put
# website backend

app = Flask("test")

@app.route("/")
def hello_world():
    return "<p>Hello World!<p>"

#Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable,
# and a "wsgi.py" or "app.py" module was not found in the current directory.