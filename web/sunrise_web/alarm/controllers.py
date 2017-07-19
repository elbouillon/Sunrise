from flask import Blueprint, render_template, request, redirect, jsonify

from .models import Alarm
from .forms import AlarmForm

alarm_blueprint = Blueprint("alarm", __name__, 
    url_prefix="/alarm", 
    template_folder="templates")

@alarm_blueprint.route("/")
def show():
    alarm = Alarm.objects.first()
    
    if alarm is not  None:
        form = AlarmForm(obj=alarm)
    else:
        form = AlarmForm()
            
    return render_template("pages/alarm.html", form=form)

@alarm_blueprint.route("/", methods=['POST'])
def save():
    alarm = Alarm.objects.first()

    if alarm is not None:
        form = AlarmForm(request.form, instance=alarm)
    else:
        form = AlarmForm(request.form)

    form.save()
        
    return redirect('/alarm')
