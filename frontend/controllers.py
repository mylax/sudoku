from flask import Flask, render_template
import requests




app = Flask(__name__)

@app.route("/")
def say_hello_too():
    return "hello, too"

@app.route("/start")
def index():
    initials = requests.get("http://app:6623/get_game_start").json()
    return render_template("display.html", initials = initials)

# @app.route("/end")
# def index():
#     initials = requests.get("http://app:6623/get_game_start").json()
#     rest = requests.get("http://app:6623/get_game_end").json()
#     return render_template("display.html", initials = initials, rest = rest)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)