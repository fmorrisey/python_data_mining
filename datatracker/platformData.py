
import json
import requests

from types import SimpleNamespace

from collections import Counter as ct
import collections as col

#names , titles = platformData.copiesPerPlatform(gameData)

class platformData(object):
    def __init__(self, game_data):
        self.game_data = game_data

    def copiesPer(game_data):   #Calls multiple functions to return two serpate lists of copies per console
        numberOfPlatforms = platformData.findUnique(game_data)
        platforms = platformData.TitlesPer(game_data)
        topPlatforms = platformData.top_Platforms(platforms, numberOfPlatforms)     #Sorts the data by top platform descending order
        platform_names, platform_titles_count = platformData.zip_Platforms(topPlatforms)
        return platform_names, platform_titles_count
   
    # Counts the number of publishers    
    def TitlesPer(json_data):
        platforms = ct(k.platform for k in json_data if k.platform)
        return platforms


    def findUnique(json_data):
    #finds unique publishers taking advantage of the set data structure
    #Constructor
        platform_set = set((""))
        
        for json_object in json_data:
            platform_set.add(json_object.platform)

        unique_platforms = len(platform_set)
        return unique_platforms

    def top_Platforms(platforms, top): 
        top_platforms = set((""))
        top_platforms = dict(ct(platforms).most_common(top))
        return top_platforms

    def zip_Platforms(platforms):
        names , titles = zip(*platforms.items())
        print(names)
        print(titles)
        return names, titles

   