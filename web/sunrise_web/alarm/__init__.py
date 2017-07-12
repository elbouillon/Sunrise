from flask import Blueprint

alarm = Blueprint('alarm', __name__)

@alarm.route('/alarm', defaults={'page': 'index'})
@alarm.route('/alarm/<page>')
def show(page):
    return "ok"

