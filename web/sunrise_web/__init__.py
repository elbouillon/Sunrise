from flask import Flask
from flask_basicauth import BasicAuth

from sunrise_web import config

# Create Flask app
app = Flask(__name__)

# Load config from config.py
app.config.from_object(config)

# Basic auth
basic_auth = BasicAuth(app)

@app.route("/")
def hello():
    return "Hello World !"