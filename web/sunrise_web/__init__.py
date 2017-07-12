from flask import Flask

from sunrise_web import config

app = Flask(__name__)
app.config.from_object(config)

@app.route("/")
def hello():
    return "Hello World !"