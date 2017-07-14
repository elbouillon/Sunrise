from flask import Blueprint, render_template, abort, request, redirect
from flask_mongoengine.wtf import model_form
from jinja2 import TemplateNotFound

from .models import Alarm
from .forms import AlarmForm

alarm = Blueprint("alarm", __name__, 
    url_prefix="/alarm", 
    template_folder="templates")


@alarm.route("/")
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


@alarm.route("/save", methods=['POST'])
def save():
    alarm = Alarm.objects.first()

    if alarm is None:
        alarm = Alarm()
  
    form = AlarmForm(request.form, instance=alarm)
    alarm = form.save()
    alarm.save()
            
    return redirect('/alarm')