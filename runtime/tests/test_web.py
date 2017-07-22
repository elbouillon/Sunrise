import httpretty
from urllib.parse import urljoin

from sunrise_runtime import config
from sunrise_runtime.web import JsonClient

config_web = config.SUNRISE_WEB
client = JsonClient(config_web)

alarm_url = urljoin(config_web['url'], config_web['alarm_request'])

@httpretty.activate
def test_get_alarm_returning_alarm():
    httpretty.register_uri(httpretty.GET, alarm_url,
                           body='{"json": "OK"}',
                           content_type="application/json")

    alarm = client.get_alarm()
    
    assert alarm is not None
    assert alarm['json'] == 'OK'