from flask.json import JSONEncoder

from sunrise_web.alarm.models import Alarm

class AlarmEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Alarm):
            alarm_dict = {
                'hour' : obj.hour,
                'minute' : obj.minute,
                'active' : obj.active,
                'day_of_week_1' : obj.day_of_week_1,
                'day_of_week_2' : obj.day_of_week_2,
                'day_of_week_3' : obj.day_of_week_3,
                'day_of_week_4' : obj.day_of_week_4,
                'day_of_week_5' : obj.day_of_week_5,
                'day_of_week_6' : obj.day_of_week_6,
                'day_of_week_7' : obj.day_of_week_7,
                'last_run_on' : obj.last_run_on.isoformat()
            }
            return alarm_dict
        else:
            JSONEncoder.default(self, obj)
