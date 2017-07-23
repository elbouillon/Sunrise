import requests
import json

from urllib.parse import urljoin
from requests.auth import HTTPBasicAuth

class Client(object):
    def __init__(self, config):
        self.__headers = {'Content-type': 'application/json'}
        self.__auth = (config['username'], config['password'])
        self.__alarm_json_url = urljoin(config['url'], config['alarm_json_request'])
        self.__alarm_update_last_run_on_url = urljoin(config['url'], config['alarm_update_last_run_on_request'])
       
    def get_alarm_as_json(self):
        response = requests.get(self.__alarm_json_url, auth=self.__auth, headers=self.__headers)
        response.raise_for_status()
        return response.json()
    
    def update_alarm_last_run_on(self, time):
        data = {'time':time}
        response = requests.post(self.__alarm_update_last_run_on_url, auth=self.__auth, headers=self.__headers, data=data)
        response.raise_for_status()
        return response