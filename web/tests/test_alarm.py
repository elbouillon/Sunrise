from test_base import BasicTest
from sunrise_web.alarm.models import Alarm

import json

class AlarmBaseTest(BasicTest):
    
    def setUp(self):
        alarm = Alarm(hour=5,minute=15, active=True, day_of_week_1=True)
        alarm.save()
    
    def tearDown(self):
        alarm = Alarm.objects.first()
        alarm.delete()

class AlarmDBTest(AlarmBaseTest):

    def test_find_one(self):
        alarm = Alarm.objects.first()

        self.assertIsNotNone(alarm)
        self.assertEquals(alarm.hour, 5)
        self.assertEquals(alarm.minute, 15)
        self.assertEquals(alarm.active, True)
        self.assertEquals(alarm.day_of_week_1, True)

class AlarmWebTest(AlarmBaseTest):

    def test_alarm_show(self):
        response = self.client.get("/alarm/")
        self.assertStatus(response, 200)

    def test_alarm_save(self):
        response = self.client.post("/alarm/", data=dict(
            hour=6,
            minute=0,
            active=True,
            day_of_week_1=True
        ))

        self.assertStatus(response, 302)

        alarm = Alarm.objects.first()

        self.assertIsNotNone(alarm) 
        self.assertEquals(alarm.hour, 6)
        self.assertEquals(alarm.minute, 0)
        self.assertTrue(alarm.active)
        self.assertTrue(alarm.day_of_week_1)
        self.assertFalse(alarm.day_of_week_2)
        self.assertFalse(alarm.day_of_week_3)
        self.assertFalse(alarm.day_of_week_4)
        self.assertFalse(alarm.day_of_week_5)
        self.assertFalse(alarm.day_of_week_6)
        self.assertFalse(alarm.day_of_week_7)
    
    def test_alarm_json(self):
        response = self.client.get("/alarm/json")
        self.assertStatus(response, 200)

        json_alarm = json.loads(response.data)
        self.assertEquals(json_alarm['hour'],5)
        self.assertEquals(json_alarm['minute'],15)
        self.assertTrue(json_alarm['active'])
        self.assertTrue(json_alarm['day_of_week_1'])
        self.assertFalse(json_alarm['day_of_week_2'])
        self.assertFalse(json_alarm['day_of_week_3'])
        self.assertFalse(json_alarm['day_of_week_4'])
        self.assertFalse(json_alarm['day_of_week_5'])
        self.assertFalse(json_alarm['day_of_week_6'])
        self.assertFalse(json_alarm['day_of_week_7'])