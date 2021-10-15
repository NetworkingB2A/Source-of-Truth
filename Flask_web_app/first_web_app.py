from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return """ <h1>Hello, World!</h1>
                I am now a WebNetDevEngineer.
                Just designing an super neat webpage.
                Just part of learn every day idea.
                I just added a export FLASK_DEBUG=1 so i dont have to restart the service every change """

@app.route("/about")
def about():
    return """ <h1>About my app, so far very basic."""

if __name__ == '__main__':
    app.run(debug=True)