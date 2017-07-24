import httpretty
from datetime import datetime
from urllib.parse import urljoin
from sure import expect

from sunrise_runtime import config
from sunrise_runtime.web import AlarmClient

config_web = config.SUNRISE_WEB
client = AlarmClient(config_web)

alarm_request = urljoin(config_web['url'], config_web['alarm_request'])
update_last_run_on_request = urljoin(config_web['url'], config_web['update_last_run_on_request'])

@httpretty.activate
def test_get_alarm_returning_alarm():
    httpretty.register_uri(httpretty.GET, alarm_request,
                           body='{"json": "OK"}',
                           content_type="application/json",
                           status=200)

    response = client.get_alarm()
    expect(response['json']).to.equal('OK')

@httpretty.activate
def test_update_alarm_last_run_on():
    httpretty.register_uri(httpretty.PUT, update_last_run_on_request,
                            body='OK',
                            content_type="application/json",
                            status=200)

    response = client.update_last_run_on(datetime.now())
    expect(response.status_code).to.equal(200)
    expect(response.text).to.equal('OK')