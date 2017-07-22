import requests
import json

from urllib.parse import urljoin
from requests.auth import HTTPBasicAuth

class JsonClient(object):
    def __init__(self, config):
        self.__headers = {'Content-type': 'application/json'}
        self.__auth = (config['username'], config['password'])
        self.__alarm_url = urljoin(config['url'], config['alarm_request'])
       
    def get_alarm(self):
        response = requests.get(self.__alarm_url, auth=self.__auth, headers=self.__headers)
        response.raise_for_status()
        return response.json()

