from types import SimpleNamespace

from collections import Counter as ct
import collections as col
class salesData(object):
    def __init__(self, game_data):
        self.game_data = game_data

    def salesPer_Global(game_data, yearMin, yearMax):
        platforms = salesData._findUniquePlatforms(game_data)
        platforms_dict = salesData._createPlatformDict(platforms)
        globalSalesRAW = salesData._salesGlobal(
            game_data, platforms_dict, yearMin, yearMax)
        globalSales = salesData._dictionaryCleaner(globalSalesRAW)
        return globalSales

    # Returns sales data and allows user to set the range of years 
    def salesPer_Regional(game_data, yearMin, yearMax):
        platforms = salesData._findUniquePlatforms(game_data)
        platforms_dict = salesData._createPlatformDict(platforms)
        regionalSalesRAW = salesData._salesRegion(
            game_data, platforms_dict, yearMin, yearMax)
        regionalSales = salesData._dictionaryCleaner(regionalSalesRAW)
        return regionalSales

    def salesOverTime(game_data, yearMin, yearMax):
        #WIP
        null = game_data
        return null

    def _salesGlobal(game_data, platforms_dict, yearMin, yearMax):
        for game in game_data:
            if type(game.year) != type(None):
                if yearMin <= game.year <= yearMax:
                    platforms_dict[f"{game.platform}"] += game.globalSales
            else:
                pass
        return platforms_dict

    # Returns a set of platforms
    def _findUniquePlatforms(game_data):
        platforms = {game.platform for game in game_data}
        return platforms

    # Creates the dictionary of all platforms
    def _createPlatformDict(platforms):  # ReturnsDict
        platforms_dict = {}
        for platform in platforms:
            platforms_dict[f'{platform}'] = 0
        return platforms_dict

    # Utility function to discover the range of years in the data set
    def _findUniqueYears(game_data, yearMin, yearMax):
        years = {}
        for game in game_data:
            if type(game.year) != type(None):
                if yearMin <= game.year <= yearMax:
                    years.append(game.year)
        return years

    # Cleans null data from the dictionary
    def _dictionaryCleaner(dictionary):
        nullEntries = []
        for entry in dictionary:
            if (dictionary[entry] == 0
                    or dictionary[entry] == type(None)):
                nullEntries.append(entry)

        for entry in nullEntries:
            del dictionary[entry]

        return dictionary

    # Creates a dictionary of regional sales
    def _salesRegion(game_data, platforms_dict, yearMin, yearMax):
        for game in game_data:
            if type(game.year) != type(None):
                if yearMin <= game.year <= yearMax:
                    platforms_dict[f"{game.platform}"] += game.globalSales
                    platforms_dict[f"{game.platform}"] += game.euSales
                    platforms_dict[f"{game.platform}"] += game.jpSales
                    platforms_dict[f"{game.platform}"] += game.otherSales

            else: pass
        return platforms_dict
    
