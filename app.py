from boggle import Boggle
from flask import Flask, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "password"
debug = DebugToolbarExtension
boggle_game = Boggle()

@app.route("/")
def display_board():
    """ Put the board into html """
    # boggle_game.make_board()
    # 
    return render_template("play_boggle.html")

