import requests
import json

from urllib.parse import urljoin
from requests.auth import HTTPBasicAuth

class AlarmClient(object):
    def __init__(self, config):
        self.__headers = {'Content-type': 'application/json'}
        self.__auth = (config['username'], config['password'])
        self.__json_url = urljoin(config['url'], config['alarm_request'])
        self.__update_last_run_on_url = urljoin(config['url'], config['update_last_run_on_request'])
       
    def get(self):
        response = requests.get(self.__json_url, auth=self.__auth, headers=self.__headers)
        response.raise_for_status()
        return response.json()
    
    def update_last_run_on(self, time):
        data = json.dumps(dict(time = time.isoformat()))
        response = requests.put(self.__update_last_run_on_url, auth=self.__auth, headers=self.__headers, data=data)
        response.raise_for_status()
        return response