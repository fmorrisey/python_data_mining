import json
import requests

from types import SimpleNamespace

from collections import Counter as ct
import collections as col

from elasticsearch import Elasticsearch
es = Elasticsearch('10.0.1.10', port=9200, timeout=30, max_retries=10, retry_on_timeout=True)

def api_request():      #Handle errors gracefully
    response = requests.get("https://api.dccresource.com/api/games")
    #json_data = response.json() if response and response.status_code == 200 else None
    #json_data = response.json() if response and response.status_code == 200 else None #Creates a dict
    json_data = str(response.content) #creates a string
    print(type(json_data))
    return json_data

def searchMeAmadeus(game_data):

    search_term = 'halo'
    """
    results = es.index(index='name_search', id=1, body=game_data)
    results = es.get(index="name_search", id=1)

    print(results['_source'])

    results = es.indices.refresh(index="name_search")
    """
    
    results = es.search(
        index=game_data,
        size=20,
        body={
            "query": {
                "match": {
                    "query": search_term,
                    "fields": ["name", "publisher"]
                }
            }
        }
    )

    for result in results:
        print(result)


game_data = api_request()
searchMeAmadeus(game_data)