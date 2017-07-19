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
    
    alarm = form.save()
    alarm.save()
        
    return redirect('/alarm', 200)

@alarm_blueprint.route("/json", methods=['GET'])
def as_json():
    alarm = Alarm.objects.first()
       
    if alarm is None:
        alarm = Alarm()
    
    return jsonify(alarm.as_json())
