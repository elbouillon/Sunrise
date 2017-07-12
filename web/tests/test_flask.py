from flask import Flask
from flask_testing import TestCase

from sunrise_web import app

class BasicTest(TestCase):
    
    def create_app(self):
        app.config['TESTING'] = True
        app.config['BASIC_AUTH_FORCE'] = False
        return app

    def test_404(self):
        response = self.client.get("/404")
        self.assertEquals(response.status_code, 404)


class AlarmTest(BasicTest):

    def test_alarm(self):
        response = self.client.get("/alarm")
        self.assertEquals(response.status_code, 200)
