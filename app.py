from boggle import Boggle
from flask import Flask, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "password"
debug = DebugToolbarExtension


boggle_game = Boggle()
on_board_dictionary = boggle_game.words


@app.route("/")
def display_board():
    """ Put the board into html """
    game_board = boggle_game.make_board()
    # letter = game_board

    session['game_board'] = game_board
    return render_template(
        "play_boggle.html",
        board=game_board
        )


word =  # whatever user sends as their guess
playable = bool(word in on_board_dictionary)


# @app.route()
# def ():
#     """ """
