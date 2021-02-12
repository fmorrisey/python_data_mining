
from api import api


def _salesPer_Global(game_data, yearMin, yearMax):
    platforms = _findUniquePlatforms(game_data)
    platforms_dict = _createPlatformDict(platforms)
    globalSalesRAW = _salesGlobal(game_data, platforms_dict, yearMin, yearMax)
    globalSales = _dictionaryCleaner(globalSalesRAW)
    return globalSales


def _salesGlobal(game_data, platforms_dict, yearMin, yearMax):
    for game in game_data:
        if type(game.year) != type(None):
            if yearMin <= game.year <= yearMax:
                platforms_dict[f"{game.platform}"] += game.globalSales
        else:
            pass
    return platforms_dict


def _findUniquePlatforms(game_data):
    platforms = {game.platform for game in game_data}
    return platforms


def _createPlatformDict(platforms):  # ReturnsDict
    platforms_dict = {}
    for platform in platforms:
        platforms_dict[f'{platform}'] = 0
    return platforms_dict


def _dictionaryCleaner(dictionary):
    nullEntries = []
    for entry in dictionary:
        if (dictionary[entry] == 0
                or dictionary[entry] == type(None)):
            nullEntries.append(entry)

    for entry in nullEntries:
        del dictionary[entry]

    return dictionary


def dictionaryPrinter(salesPer):
    for game, sales in salesPer.items():
        print(game, ":", sales)


game_data = api.requests_NameSpace("https://api.dccresource.com/api/games")
salesPer = _salesPer_Global(game_data, 2013, 2021)
dictionaryPrinter(salesPer)
