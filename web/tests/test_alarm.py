import json

from datetime import datetime

from test_base import BasicTest
from sunrise_web.alarm.models import Alarm

class AlarmBaseTest(BasicTest):

    expected_time = datetime(2017, 7, 23, 21, 40, 0, 0).isoformat()

    def setUp(self):
        alarm = Alarm(hour=5,minute=15, active=True, day_of_week_1=True, last_run_on=self.expected_time)
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
        self.assertEquals(alarm.last_run_on.isoformat(), self.expected_time)

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
        self.assertIsNone(alarm.last_run_on)
    
    def test_alarm_json(self):
        response = self.client.get('/alarm/json', content_type='application/json')
        self.assertStatus(response, 200)

        json_alarm = json.loads(response.data)
        alarm = Alarm.objects.first()

        
        self.assertEquals(json_alarm['hour'],alarm.hour)
        self.assertEquals(json_alarm['minute'], alarm.minute)
        self.assertEquals(json_alarm['active'], alarm.active)
        self.assertEquals(json_alarm['day_of_week_1'], alarm.day_of_week_1)
        self.assertEquals(json_alarm['day_of_week_2'], alarm.day_of_week_2)
        self.assertEquals(json_alarm['day_of_week_3'], alarm.day_of_week_3)
        self.assertEquals(json_alarm['day_of_week_4'], alarm.day_of_week_4)
        self.assertEquals(json_alarm['day_of_week_5'], alarm.day_of_week_5)
        self.assertEquals(json_alarm['day_of_week_6'], alarm.day_of_week_6)
        self.assertEquals(json_alarm['day_of_week_7'], alarm.day_of_week_7)
        self.assertEquals(json_alarm['last_run_on'], alarm.last_run_on.isoformat())

    def test_update_last_run_on(self):
        time = datetime(2017, 7, 23, 21, 40, 0, 0).isoformat()
        data = json.dumps(dict(time=time))

        response = self.client.put('/alarm/last_run_on',
            content_type='application/json',
            data=data)
        self.assertStatus(response, 200)
        
        alarm = Alarm.objects.first()   
        self.assertEquals(alarm.last_run_on.isoformat(), time)