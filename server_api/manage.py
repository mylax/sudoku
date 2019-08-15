from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData, select, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
import json
import psycopg2
from flask import Flask, jsonify
import requests
import pandas as pd
from random import shuffle

def sudoku_values(initial):
    db_string = "postgres://testusr:passwor@localhost:7435/testdb"
    db = create_engine(db_string)
    base = declarative_base()
    class Sudoku(base):
        __tablename__ = 'sudoku'
        val = Column(Integer)
        initial = Column(Integer)
        index = Column(Integer, primary_key = True)
        id_game = Column(Integer)

    Session = sessionmaker(db)
    session = Session()
    base.metadata.create_all(db)

    ids = []
    for value in session.query(Sudoku.id_game).distinct():
        ids.append(value)
    shuffle(ids)
    id_to_filter = ids[0][0]

    initials = {}
    for u in session.query(Sudoku).filter(Sudoku.id_game == id_to_filter).filter(Sudoku.initial.in_(initial)).all():
        initials[u.index] = u.val
    session.close()

    return initials


app = Flask(__name__)


@app.route("/get_game_start", methods=['GET'])
def game_start():
    initials = sudoku_values([1])
    return jsonify(initials)

@app.route("/get_game_end")
def game_end():
    initials = sudoku_values([0, 1])
    return jsonify(initials)

@app.route("/start")
def index():
    initials = requests.get("http://localhost:5000/create_sudoku").json()
    dat = pd.DataFrame(initials)
    dat["id_game"] = hash(json.dumps(initials))
    dat.index += 1
    db_string = "postgresql://testusr:passwor@localhost:7435/testdb"
    engine = create_engine(db_string)
    dat.index.name = "index"
    dat.to_sql("sudoku", engine, if_exists = "append")
    return "wrote sudoku game to db"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6002)