from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

PORT = 80
ADDRESS = '0.0.0.0'