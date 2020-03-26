from solver import find_sudoku
import json
from flask import Flask, jsonify
from flask_restplus import Resource, Api
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/create_sudoku")
def get():
    sudoku = find_sudoku()
    return jsonify(sudoku.to_dict(orient = "list"))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
