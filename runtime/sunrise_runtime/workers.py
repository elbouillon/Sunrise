import threading
import time
import re
from datetime import datetime

import config
from web import JsonClient

class CheckAlarmWorker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__client = JsonClient(config.SUNRISE_WEB)

    def run(self):
        alarm_match = False

        while not alarm_match:
            alarm = self.__client.get_alarm()

            if alarm is not None and alarm['active'] == True:
                alarm_regex = self.__get_alarm_regex(alarm)
                current_time_str = self.__get_current_time_str()

                if re.match(alarm_regex, current_time_str):
                    alarm_match = True

            if not alarm_match:            
                time.sleep(3)
    
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
