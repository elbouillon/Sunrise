from test_base import BasicTest
from sunrise_web.alarm.models import Alarm

class AlarmDBTest(BasicTest):

    def setUp(self):
        alarm = Alarm(hour=5,minute=15, active=True, day_of_week_1=True)
        alarm.save()
    
    def tearDown(self):
        alarm = Alarm.objects.first()
        alarm.delete()

    def test_find_one(self):
        alarm = Alarm.objects.first()

        self.assertIsNotNone(alarm)
        self.assertEquals(alarm.hour, 5)
        self.assertEquals(alarm.minute, 15)
        self.assertEquals(alarm.active, True)
        self.assertEquals(alarm.day_of_week_1, True)

class AlarmTest(BasicTest):

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
        self.assertEquals(alarm.day_of_week_1, True)
        self.assertEquals(alarm.day_of_week_2, False)
        self.assertEquals(alarm.day_of_week_3, False)
        self.assertEquals(alarm.day_of_week_4, False)
        self.assertEquals(alarm.day_of_week_5, False)
        self.assertEquals(alarm.day_of_week_6, False)
        self.assertEquals(alarm.day_of_week_7, False)