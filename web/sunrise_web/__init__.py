from flask import Flask
from flask_basicauth import BasicAuth
from flask_mongoengine import MongoEngine
from flask_debugtoolbar import DebugToolbarExtension

from sunrise_web import config
from sunrise_web.encoders import AlarmEncoder
from sunrise_web.alarm.controllers import alarm_blueprint

# MongoEngine
db = MongoEngine()

def create_app(**config_overrides):

    # Create Flask app
    app = Flask(__name__)

    # Load config from config.py
    app.config.from_object(config)
    
    # Apply overrides
    app.config.update(config_overrides)

    # Basic auth
    BasicAuth(app)

     # Setup the database.
    db.init_app(app)
  
    # Register blueprints
    app.register_blueprint(alarm_blueprint)

    app.json_encoder = AlarmEncoder

    if config.MONGO_DEBUG_TB == True:
        toolbar = DebugToolbarExtension(app)

    return app