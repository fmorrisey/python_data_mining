from types import SimpleNamespace

from collections import Counter as ct
import collections as col

#names , titles = platformData.copiesPerPlatform(gameData)
class platformData(object):
    def __init__(self, game_data):
        self.game_data = game_data

    # Calls multiple functions to return two serpate lists of copies per console
    def copiesPer_Dict(game_data):
        numberOfPlatforms = platformData._findUniquePlatforms(
            game_data, 2013, 2021)
        platforms = platformData._titlesPer(game_data)
        # Sorts the data by top platform descending order
        topPlatforms = platformData._top_Platforms(
            platforms, numberOfPlatforms)
        return topPlatforms  # Returns Dict

    # Calls multiple functions to return two serpate lists of copies per console
    def copiesPer_Lists(game_data):
        numberOfPlatforms = platformData._findUniquePlatforms(
            game_data, 2013, 2021)
        platforms = platformData._titlesPer(game_data)
        # Sorts the data by top platform descending order
        topPlatforms = platformData._top_Platforms(
            platforms, numberOfPlatforms)
        platform_names, platform_titles_count = platformData._zip_Platforms(
            topPlatforms)  # Pulls the dictionary apart
        return platform_names, platform_titles_count  # Return Lists

    # Calls multiple functions to return two serpate lists of copies per console
    def salesPer_Dict(game_data):
        numberOfPlatforms = platformData._findUniquePlatforms(
            game_data, 2013, 2021)
        platforms = platformData._titlesPer(game_data)
        # Sorts the data by top platform descending order
        topPlatforms = platformData._top_Platforms(
            platforms, numberOfPlatforms)
        salesPer_Dict = platformData._salesPerV1(game_data, topPlatforms)
        return topPlatforms  # Returns Dict

    # Counts the number of platforms
    def _titlesPer(json_data):
        platforms = ct(k.platform for k in json_data if k.platform)
        return platforms

    def _findUniquePlatforms(json_data, yearMin, yearMax):
        # finds unique platforms taking advantage of the set data structure
        # Constructor
        platform_set = set((""))

        for platform in json_data:
            if type(platform.year) != type(None):
                if yearMin <= platform.year <= yearMax:
                    platform_set.add(platform.platform)
                else:
                    pass
            else:
                pass

        unique_platforms = len(platform_set)
        return unique_platforms

    def _findUniquePublishers(json_data, yearMin, yearMax):
        #finds unique publishers taking advantage of the set data structure
        #Constructor
        publisher_set = set((""))

        for json_object in json_data:
            if yearMin <= json_object.year <= yearMax:
                publisher_set.add(json_object.publisher)

        unique_platforms = len(publisher_set)
        return unique_platforms

    def _top_Platforms(platforms, top):
        top_platforms = set((""))
        top_platforms = dict(ct(platforms).most_common(top))
        return top_platforms

    def _zip_Platforms(platforms):
        names, titles = zip(*platforms.items())
        print(names)
        print(titles)
        return names, titles
