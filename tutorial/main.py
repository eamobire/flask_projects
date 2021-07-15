from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!<h1>" \
           "<p> This is a paragraph </p>" \
           "<img src='https://media.giphy.com/media/M8PxVICV5KlezP1pGE/giphy.gif' width=200>"


@app.route("/bye")
def bye():
    return "bye"


@app.route("/username/<name>")
def greet(name):
    return f"Hello there! {name}"


if __name__ == "__main__":
    app.run(debug=True)
