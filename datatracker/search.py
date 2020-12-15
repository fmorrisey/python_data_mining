import json
import requests
from collections import defaultdict as dd

def api_request(): #Handle errors gracefully
    response = requests.get("https://api.dccresource.com/api/games")
    game_data = json.loads(response.content, object_hook=lambda d:SimpleNamespace(**d))\
        if response and response.status_code == 200 else None
    return game_data


def searchByName(game_data, *args):

    helperdict = dd.defaultdict(set)

    for game, name in game_data.items():
        for name in game_data.split('+'):
            helperdict[name].add(game)



game_data = api_request()    