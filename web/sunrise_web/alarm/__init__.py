from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from .forms import AlarmForm

alarm = Blueprint("alarm", __name__, 
    url_prefix="/alarm", 
    template_folder="templates")


@alarm.route("/", strict_slashes=False)
def index():
    try:

        form = AlarmForm()
        form.time=666

        return render_template("pages/alarm.html",form=form)
    except TemplateNotFound:
        abort(404)
    
@alarm.route("/<int:alarm_id>", methods=['GET'])
def show(alarm_id):
    pass
   # try:
   #     return render_template("pages/alarm.html".format(page))
   # except TemplateNotFound:
   #     abort(404)