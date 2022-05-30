# MODULES / LIBRAIRES
from flask import Flask, render_template
# from venv.libs.python38.site_packages import flask

# API
from psqlapi import connect, post_bot, post_user, get_bot, get_user, put_bot, put_user

app = Flask(__name__)



# home
@app.route("/")
def render_home():
    return render_template("index.html", name="Inicio")

# bot
@app.route("/add-bot")
def render_bot():
    return render_template("bot.html", name="El Hijo")

# profile
@app.route("/add-nor")
def render_normas():
    return render_template("normas/normas.html", name="Normas")

# library
@app.route("/add-lib")
def render_files():
    return render_template("library.html", name="ADDeditorial")



# 404
@app.errorhandler(404)
def invalid_route(e):
    return render_template("notfound.html", name="Not Found")



if __name__ == "__main__":
    app.run(debug=True)
