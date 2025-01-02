from flask import Flask
app = Flask(__name__)


@app.route('/<string:name>')
def index(name):
    return f'<h1>Hello, {name}!</h1>'


@app.route('/hello')
def hello():
    return 'Hello, World!'

