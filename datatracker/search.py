import json
import requests
from collections import defaultdict as dd
from types import SimpleNamespace

# Case insensitive string searchByName will accommodate incorrect casings of letters ex HaLo reACH
# Also will return multiple matches so, returns all halo games, and all 1468 versions of Call of Duty
class search:
    def __init__(self):
        self.__init__ = True

    def searchByName(game_data, search_term):
        results = []

        for game in game_data:
            if search_term.casefold() in game.name.casefold():
                results.append(game)
                break
        
        return results, len(results)
    