from flask import Flask
from flask_basicauth import BasicAuth

from sunrise_web import config
from sunrise_web.alarm import alarm

# Create Flask app
app = Flask(__name__)

# Load config from config.py
app.config.from_object(config)

# Basic auth
basic_auth = BasicAuth(app)

# Register blueprints
app.register_blueprint(alarm)