from datetime import datetime

from test_base import BasicTest

from sunrise_web.alarm.models import Alarm


class AlarmDBTest(BasicTest):

    def setUp(self):
        alarm = Alarm(time=500, active=True, day_1=True)
        alarm.save()
    
    def tearDown(self):
        alarm = Alarm.objects.first()
        alarm.delete()

    def test_find_one(self):
        alarm = Alarm.objects.first()
        self.assertIsNotNone(alarm)
        self.assertEquals(alarm.time, 500)
        self.assertEquals(alarm.active, True)
        self.assertEquals(alarm.day_1, True)

    