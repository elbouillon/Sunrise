from flask import Blueprint, render_template, request, redirect, jsonify, abort

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
    form.populate_obj(alarm)

    alarm.last_run_on = None
    alarm.save()

    return redirect('/alarm')

@alarm_blueprint.route("/json", methods=['GET'])
def get_alarm_as_json():
    alarm = Alarm.objects.first()
    
    if alarm is None:
        abort(404)

    return jsonify(alarm)

@alarm_blueprint.route("/last_run_on", methods=['PUT'])
def update_last_run_on():
    alarm = Alarm.objects.first()
    
    if alarm is None:
        abort(404)
   
    json = request.get_json()
    if json is None:
        abort(400)

    alarm.last_run_on = json['time']
    alarm.save()
   
    return "OK", 200