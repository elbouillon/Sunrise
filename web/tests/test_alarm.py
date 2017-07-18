from datetime import datetime

from test_base import BasicTest

from sunrise_web.alarm.models import Alarm


class AlarmDBTest(BasicTest):

    def setUp(self):
        alarm = Alarm(time="05:00", active=True, day_1=True)
        alarm.save()
    
    def tearDown(self):
        alarm = Alarm.objects.first()
        alarm.delete()

    def test_find_one(self):
        alarm = Alarm.objects.first()
        self.assertIsNotNone(alarm)
        self.assertEquals(alarm.time, "05:00")
        self.assertEquals(alarm.active, True)
        self.assertEquals(alarm.day_1, True)

class AlarmTest(BasicTest):

    def test_alarm_show(self):
        response = self.client.get("/alarm/")
        self.assertStatus(response, 200)

    def test_alarm_save(self):
        response = self.client.post("/alarm/", data=dict(
            time= "05:00",
            active=True,
            day_1=True
        ), follow_redirects=True)

        self.assertStatus(response, 200)
        alarm = Alarm.objects.first()
        self.assertIsNotNone(alarm)
        self.assertEquals(alarm.time, "05:00")
        self.assertTrue(alarm.active)
        self.assertEquals(alarm.day_1, True)

