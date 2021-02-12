import json
import requests
from types import SimpleNamespace


class api:
    def __init__(self):
        self.__init__ = True

    def requests_NameSpace(apiUrl):  # Handle errors gracefully
        response = requests.get(apiUrl)
        print(type(response.content))
        json_data = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))\
            if response and response.status_code == 200 else None
        print(type(json_data))
        return json_data  # Returns Namespace response

    def requests_JSONList(apiUrl):  # Handle errors gracefully
        response = requests.get(apiUrl)
        json_data = response.json() \
            if response and response.status_code == 200 else None
        print(type(json_data))
        return json_data  # Returns a List

    def requests_JSONDict(apiUrl):  # Handle errors gracefully
        response = requests.get(apiUrl)
        json_data = response.json() \
            if response and response.status_code == 200 else None
        print(type(json_data))
        return json_data  # Returns a Dict

    # Attempt to reduce external api consumption loads local copy
    # Lowering Michael Terril's bandwidth bill, it's not much but it's honest work
    def request_local(path):
        with open(path) as local_data:
            # Converts io.TextWrapper -> dict -> str -> list.Obj
            data_dict = json.load(local_data)
            data_str = json.dumps(data_dict)
            json_data = json.loads(data_str, object_hook=lambda d: SimpleNamespace(**d))
        
        return json_data
            
