from flask import Blueprint, render_template, request, redirect, jsonify

from .models import Alarm
from .forms import AlarmForm

alarm_blueprint = Blueprint("alarm", __name__, 
    url_prefix="/alarm", 
    template_folder="templates")

@alarm_blueprint.route("/")
def show():
    alarm = Alarm.objects.first()
    
    if alarm is None:
        alarm = Alarm()

    form = AlarmForm(obj=alarm)

    return render_template("pages/alarm.html", form=form)

@alarm_blueprint.route("/", methods=['POST'])
def save():
    alarm = Alarm.objects.first()

    if alarm is None:
        alarm = Alarm()

    form = AlarmForm(request.form, instance=alarm)
    form.save()

    return redirect('/alarm')

@alarm_blueprint.route("/json", methods=['GET'])
def to_json():
    alarm = Alarm.objects.first()
    
    if alarm is None:
        alarm = Alarm()
    
    return jsonify(alarm)

@alarm_blueprint.route("/last_run_on", methods=['PUT'])
def update_last_run_on():
    alarm = Alarm.objects.first()

    if alarm is None:
         abort(404)
     
    alarm.last_run_on = request.form['time']
    alarm.save()

    return "OK", 200