import json
import requests
from collections import defaultdict as dd
from types import SimpleNamespace

def api_request(): #Handle errors gracefully
    response = requests.get("https://api.dccresource.com/api/games")
    game_data = json.loads(response.content, object_hook=lambda d:SimpleNamespace(**d))\
        if response and response.status_code == 200 else None
    return game_data

# Case insensitive string searchByName will accommodate incorrect casings of letters ex HaLo: reACH
def searchByName(game_data, search_term):
    results = []

    for game in game_data:
        if search_term.casefold() in game.name.casefold():
            results.append(game)
    


    return results, len(results)


def searchByID(results, game_ID):
    idvResults = []

    for game in results:
        if game._id == game_ID:
            idvResults.append(game)
        else: pass
    
    return idvResults

game_data = api_request()
results, hits = searchByName(game_data, "mario")
idvResults = searchByID(game_data, '5faac565db090e1a5c2dfc19')

for game in idvResults:
    print(game)

