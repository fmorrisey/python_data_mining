import json
import requests
from types import SimpleNamespace


class api:
    def __init__(self):
        self.__init__ = True

    def requests_NameSpace(apiUrl): #Handle errors gracefully
        response = requests.get(apiUrl)
        json_data = json.loads(response.content, object_hook=lambda d:SimpleNamespace(**d))\
            if response and response.status_code == 200 else None
        print(type(json_data))
        return json_data

    def requests_JSONDict(apiUrl): #Handle errors gracefully
        response = requests.get(apiUrl)
        json_data = json.loads(response.content, object_hook=lambda d:SimpleNamespace(**d))\
            if response and response.status_code == 200 else None
        return json_data