from flask_mongoengine.wtf import model_form

from .models import Alarm

AlarmForm = model_form(Alarm)
