from flask_wtf import Form
from wtforms import IntegerField

class AlarmForm(Form):
    time = IntegerField('Time')