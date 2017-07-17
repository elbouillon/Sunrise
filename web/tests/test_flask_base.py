from flask import Flask
from flask_testing import TestCase

from sunrise_web import create_app as create_app_base, db

class BasicTest(TestCase):
    
    def create_app(self):
        return create_app_base(
            TESTING = True,
            BASIC_AUTH_FORCE = False,
            MONGODB_SETTINGS = {
                'db': 'sunrise_test',
                'host': 'mongodb://192.168.99.100/sunrise_test',
            }
        )

    def tearDown(self):
        db.connection.drop_database('sunrise_test')

    def test_404(self):
        response = self.client.get("/404")
        self.assertEquals(response.status_code, 404)



