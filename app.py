from flask import Flask, request, render_template, redirect, flash, jsonify
from flask import session, make_response
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "IT'S A SECRET"

boggle_game = Boggle()

@app.route("/")
def display_board():
    """display game board"""
    board = boggle_game.make_board()
    session["board"] = board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays" ,0)
    return render_template("board.html", board=board, highscore=highscore, nplays=nplays)

@app.route("/valid")
def check_valid_word():
    """check valid word"""
    word = request.args["guess_word"]#chunmei: why can not use request.form in here?
    board = session["board"]
    isvalid = boggle_game.check_valid_word(board, word)

    return jsonify({'result': isvalid})

@app.route("/endgame", methods=["POST"])
def end_game():
    """Receive score, update play times and highest score"""
    score = request.json["score"] #request.json = {'score': 2}
    # import pdb
    # pdb.set_trace()

    highscore = session.get("highscore", 0)
    nplays = session.get("nplays" ,0)

    session['highscore'] = max(score, highscore)
    session['nplays'] = nplays + 1

    return jsonify({'nplays' : session['nplays'], 'highscore' : session['highscore']})