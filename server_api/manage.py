from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData, select, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
import json
import psycopg2
from flask import Flask, jsonify
import requests



def sudoku_values(initial):
    db_string = "postgres://testusr:passwor@postgres:5432/testdb"
    db = create_engine(db_string)
    base = declarative_base()
    class Sudoku(base):
        __tablename__ = 'sudoku'
        val = Column(Integer)
        initial = Column(Integer)
        id = Column(Integer, primary_key = True)

    Session = sessionmaker(db)
    session = Session()
    base.metadata.create_all(db)

    initials = {}

    for u in session.query(Sudoku).filter(Sudoku.initial.in_(initial)).all():
        initials[u.id] = u.val
    session.close()

    return initials



def write_to_db(sudoku):
    return "nothing yet"





app = Flask(__name__)



# @main.route("/", methods = ["POST"])
# def my_form_post():
#     result = []
#     for i in range(1, 82):
#         text = request.form['testing' + str(i)]
#         result.append(text)
#     result = "".join(result)
#     if result == "".join([str(rest[key]) for key in rest]):
#         return "success!"
#     return "failure!"


@app.route("/get_game_start", methods=['GET'])
def game_start():
    initials = sudoku_values([1])
    return jsonify(initials)

@app.route("/get_game_end")
def game_end():
    initials = sudoku_values([0, 1])
    return jsonify(initials)

@app.route("/")
def say_hello():
    return "hello"

@app.route("/start")
def index():
    initials = requests.get("http://app3:6624/get_game_start").json()
    write_to_db(initials)
    return "game is saved to db"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6623)