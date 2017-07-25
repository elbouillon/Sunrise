import threading
import time
import re
import dateutil.parser
from datetime import datetime


from web import AlarmClient

class CheckAlarmWorker(threading.Thread):
    def __init__(self, config):
        threading.Thread.__init__(self)
        self.__alarm_client = AlarmClient(config.SUNRISE_WEB)

    def run(self):
        match = False

        while not match:
            time.sleep(1)
            try:
                alarm = self.__alarm_client.get()
                match = self.__check_alarm(alarm)
            except:
                print 'Unexpected error:', sys.exc_info()[0]

        try:
            now = datetime.now().replace(second=0, microsecond=0)  
            self.__alarm_client.update_last_run_on(now)
        except:
            print('Could not update alarm last_run_on time')
            raise

    def __check_alarm(self, alarm):
        if alarm is None or alarm['active'] == False:
            return False

        if 'last_run_on' in alarm:
            last_run_on = dateutil.parser.parse(alarm['last_run_on'])
            timedelta = datetime.now() - last_run_on
            if timedelta.total_seconds() < 60:
                return False

        alarm_regex = self.__get_alarm_regex(alarm)
        current_time_str = self.__get_current_time_str()

        return re.match(alarm_regex, current_time_str)

    def __get_alarm_regex(self, alarm):
        hour = alarm['hour']
        minute = alarm['minute']
        days_of_week = []

        if alarm['day_of_week_1']: days_of_week.append('0')
        if alarm['day_of_week_2']: days_of_week.append('1')
        if alarm['day_of_week_3']: days_of_week.append('2')
        if alarm['day_of_week_4']: days_of_week.append('3')
        if alarm['day_of_week_5']: days_of_week.append('4')
        if alarm['day_of_week_6']: days_of_week.append('5')
        if alarm['day_of_week_7']: days_of_week.append('6')
        days_of_week_str = ''.join(days_of_week)

        return '^({} {} [{}])$'.format(hour, minute, days_of_week_str)
    
    def __get_current_time_str(self):
        now = datetime.now()
        today = datetime.today()
        return '{} {} {}'.format(now.hour, now.minute, today.weekday())