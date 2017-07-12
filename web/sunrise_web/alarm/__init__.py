from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

alarm = Blueprint("alarm", __name__, 
    url_prefix="/alarm", 
    template_folder="templates")


@alarm.route("/", defaults={"page": "index"}, strict_slashes=False)
@alarm.route("/<page>")
def show(page):
    try:
        return render_template("pages/{}.html".format(page))
    except TemplateNotFound:
        abort(404)