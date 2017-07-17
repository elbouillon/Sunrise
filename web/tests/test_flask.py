from flask import Flask

from test_base import BasicTest

class FlaskTest(BasicTest):

    def test_404(self):
        response = self.client.get("/404")
        self.assertEquals(response.status_code, 404)