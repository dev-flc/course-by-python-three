from flask import Flask 


app = Flask(__name__)


@app.route('/')


def hello_world():
    """ Example """
    return "hola mundo"


if __name__ == '__main__':
    help(hello_world)
    app.run(host='127.0.0.1', port=80)