from flask import Flask
from flask_basicauth import BasicAuth
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine

from sunrise_web import config
from sunrise_web.alarm import alarm

# Create Flask app
app = Flask(__name__)

# Load config from config.py
app.config.from_object(config)

# Basic auth
BasicAuth(app)

# Bootstrap
Bootstrap(app)

# MongoEngine
db = MongoEngine(app)

# Register blueprints
app.register_blueprint(alarm)