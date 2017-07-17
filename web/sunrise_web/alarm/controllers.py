from flask import Blueprint, render_template, abort, request, redirect
from flask_mongoengine.wtf import model_form
from jinja2 import TemplateNotFound

from .models import Alarm
from .forms import AlarmForm

alarm_blueprint = Blueprint("alarm", __name__, 
    url_prefix="/alarm", 
    template_folder="templates")


@alarm_blueprint.route("/")
def show():
    try:
        alarm = Alarm.objects.first()
    
        if alarm is not  None:
            form = AlarmForm(obj=alarm)
        else:
            form = AlarmForm()
            
        return render_template("pages/alarm.html", form=form)
    except TemplateNotFound:
        abort(404)


@alarm_blueprint.route("/", methods=['POST'])
def save():
    try:
        alarm = Alarm.objects.first()

        if alarm is not None:
            form = AlarmForm(request.form, instance=alarm)
        else:
            form = AlarmForm(request.form)
    
        alarm = form.save()
        alarm.save()
        
        return render_template("pages/alarm.html", form=form)
    except TemplateNotFound:
        abort(404)