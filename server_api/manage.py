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
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://testusr:passwor@db:5432/testdb"
db = SQLAlchemy(app)

class Sudoku(db.Model):
    val = Column(db.Integer)
    initial = Column(db.Integer)
    index = Column(db.Integer, primary_key = True)
    id_game = Column(db.Integer, primary_key = True)

@app.route("/get_ids", methods=["GET"])
@cross_origin()
def game_ids():
    all_ids = [x.id_game for x in Sudoku.query.all()]
    unique_ids = len(list(set(all_ids)))
    unique_ids = list(range(unique_ids))
    return jsonify(unique_ids)


@app.route("/get_game_start/<int:id>", methods=['GET'])
@cross_origin()
def game_start(id):
    all_ids = [x.id_game for x in Sudoku.query.all()]
    unique_ids = list(set(all_ids))
    query = Sudoku.query.filter_by(id_game=unique_ids[id], initial = 1).all()
    result = {}
    for x in query:
        result[x.index] = x.val
    return jsonify(result)

@app.route("/get_game_end/<int:id>", methods=['GET'])
def game_end(id):
    all_ids = [x.id_game for x in Sudoku.query.all()]
    unique_ids = list(set(all_ids))
    query = Sudoku.query.filter_by(id_game=unique_ids[id]).all()
    result = {}
    for x in query:
        result[x.index] = x.val
    return jsonify(result)

@app.route("/start")
def index():
    initials = requests.get("http://su_slvr:5000/create_sudoku").json()
    dat = pd.DataFrame(initials)
    dat["id_game"] = hash(json.dumps(initials))
    dat.index += 1
    db_string = "postgresql://testusr:passwor@db:5432/testdb"
    engine = create_engine(db_string)
    dat.index.name = "index"
    dat.to_sql("sudoku", engine, if_exists = "append")
    return "wrote sudoku game to db"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')