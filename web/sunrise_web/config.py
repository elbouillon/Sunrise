SECRET_KEY = 'BLA BLA BLA'

# Activate Debugger
DEBUG = True

# Basic Auth
BASIC_AUTH_USERNAME = 'sunrise'
BASIC_AUTH_PASSWORD = 'sunrise'
BASIC_AUTH_FORCE = True

# Bootstrap
BOOTSTRAP_USE_MINIFIED = True
BOOTSTRAP_SERVE_LOCAL = True

# Flask WTF 
WTF_CSRF_ENABLED = False

# MongoDB
MONGODB_SETTINGS = {
    'db': 'sunrise_db',
    'host': 'mongodb://192.168.99.100/sunrise',
}

# Mongo Debug Toolbar
MONGO_DEBUG_TB = False
DEBUG_TB_PANELS = ['flask_mongoengine.panels.MongoDebugPanel']
