from flask import Flask
from flask_testing import TestCase

from sunrise_web import app, db
from sunrise_web.alarm.models import Alarm

class BasicTest(TestCase):
    
    def create_app(self):
        app.config['TESTING'] = True
        app.config['BASIC_AUTH_FORCE'] = False
        app.config['MONGODB_SETTINGS'] = {
            'db': 'sunrise',
            'host': 'mongodb://192.168.99.100/sunrise',
        }
        return app

    def tearDown(self):
        db.connection.drop_database('sunrise')

    def test_404(self):
        response = self.client.get("/404")
        self.assertEquals(response.status_code, 404)

class AlarmDBTest(BasicTest):

    def setUp(self):
        alarm = Alarm(500)
        alarm.save()
    
    def tearDown(self):
        alarm = Alarm.objects.first()
        alarm.delete()

    def test_find_one(self):
        alarm = Alarm.objects.first()
        self.assertIsNotNone(alarm)
        self.assertEquals(alarm.time, 500)

class AlarmTest(BasicTest):

    def test_alarm_show(self):
        response = self.client.get("/alarm/")
        self.assertStatus(response, 200)

    def test_alarm_save(self):
        response = self.client.post("/alarm/save", data=dict(
            time=666
        ), follow_redirects=True)
        
        self.assertStatus(response, 200)
        alarm = Alarm.objects.first()
        self.assertIsNotNone(alarm)
        self.assertEquals(alarm.time, 666)

