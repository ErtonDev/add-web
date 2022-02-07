# MODULES / LIBRAIRES
from flask import Flask, render_template

# API
from psqlapi import connect, post_bot, post_user, get_bot, get_user, put_bot, put_user

app = Flask(__name__)

# home
@app.route("/")
def index():
    return render_template("index.html", name="home")

if __name__ == "__main__":
    app.run(debug=True)
