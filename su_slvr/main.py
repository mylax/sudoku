from solver import find_sudoku
import json
from flask import Flask, jsonify
from flask_restplus import Resource, Api



app = Flask(__name__)
api = Api(app)


@api.route("/create_sudoku")
# @api.doc(params={"id": "An ID"})
class CreateSudoku(Resource):
    def get(self):
        sudoku = find_sudoku()
        return jsonify(sudoku.to_dict(orient = "list"))
    # @api.doc(responses={403: "Not Authorized"})
    # def post(self, id):
    #     api.abort(403)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
