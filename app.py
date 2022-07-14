from flask import Flask, request, render_template, redirect, flash, jsonify
from flask import session, make_response
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "IT'S A SECRET"

boggle_game = Boggle()

@app.route("/")
def display_board():
    """display board"""
    board = boggle_game.make_board()
    session["board"] = board
    return render_template("board.html", board=board)

@app.route("/valid")
def check_valid_word():
    """check valid word"""
    word = request.args['guess_word']
    board = session["board"]
    isvalid = boggle_game.check_valid_word(board, word)

    return jsonify({'result': isvalid})

