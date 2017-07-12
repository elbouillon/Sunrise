from flask import Flask
from flask_testing import TestCase

from sunrise_web import app

class BasicTest(TestCase):
    
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_hello(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

    def test_404(self):
        response = self.client.get("/404")
        self.assertEquals(response.status_code, 404)