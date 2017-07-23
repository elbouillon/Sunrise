import httpretty
from datetime import datetime
from urllib.parse import urljoin
from sure import expect

from sunrise_runtime import config
from sunrise_runtime.web import Client

config_web = config.SUNRISE_WEB
client = Client(config_web)

alarm_json_request = urljoin(config_web['url'], config_web['alarm_json_request'])
alarm_update_last_run_on_request = urljoin(config_web['url'], config_web['alarm_update_last_run_on_request'])

@httpretty.activate
def test_get_alarm_returning_alarm():
    httpretty.register_uri(httpretty.GET, alarm_json_request,
                           body='{"json": "OK"}',
                           content_type="application/json")

    alarm = client.get_alarm_as_json()
    expect(alarm['json']).to.equal('OK')

@httpretty.activate
def test_update_alarm_last_run_on():
    httpretty.register_uri(httpretty.POST, alarm_update_last_run_on_request,
                           body='OK',
                           status=200,
                           content_type="application/json")

    response = client.update_alarm_last_run_on(datetime.now())
    expect(response.status_code).to.equal(200)
    expect(response.text).to.equal('OK')