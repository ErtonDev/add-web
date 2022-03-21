# MODULES / LIBRAIRES
from flask import Flask, render_template
# from venv.libs.python38.site_packages import flask

# API
from psqlapi import connect, post_bot, post_user, get_bot, get_user, put_bot, put_user

app = Flask(__name__)



# home
@app.route("/")
def index():
    return render_template("index.html", name="Home")

# bot
@app.route("/bot")
def bot():
    return render_template("bot.html", name="El Hijo")

# profile
@app.route("/profile")
def profile():
    return render_template("profile.html", name="Profile")

# library
@app.route("/library")
def library():
    return render_template("library.html", name="ADDeditorial")



if __name__ == "__main__":
    app.run(debug=True)
