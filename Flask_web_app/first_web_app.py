from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """ <h1>Hello, World!</h1>
                I am now a WebNetDevEngineer.
                Just designing an super neat webpage.
                Just part of learn every day idea.
                I just added a export FLASK_DEBUG=1 so i dont have to restart the service every change """


if __name__ == '__main__':
    app.run(debug=True)