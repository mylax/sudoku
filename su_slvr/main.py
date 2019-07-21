from solver import find_sudoku
import json
from flask import Flask, jsonify




app = Flask(__name__)



@app.route("/get_game_start", methods=['GET'])
def game_start():
    sudoku = find_sudoku()
    return jsonify(sudoku.to_dict(orient = 'list'))

@app.route("/")
def say_hello():
    return "hello 3"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6624)