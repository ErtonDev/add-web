# MODULES / LIBRAIRES
from flask import Flask, render_template

# API
from psqlapi import connect, post, get, put

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("templates/index.html", name="home")
