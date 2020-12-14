import json
import requests


def api_request(): #Handle errors gracefully
    response = requests.get("https://api.dccresource.com/api/games")
    game_data = json.loads(response.content, object_hook=lambda d:SimpleNamespace(**d))\
        if response and response.status_code == 200 else None
    return game_data


def searchByName(game_data, query):

    for game in game_data:
        if game.name == query:
            



game_data = api_request()    