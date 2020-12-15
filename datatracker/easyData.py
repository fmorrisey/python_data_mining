from api import api as api
from types import SimpleNamespace
import json

def byConsolePerDecade(game_data):
    #years = salesData.decades(game_data)
    dec1980 = groupByDecade(game_data)
    listPrinter(dec1980)
    pass

    return dec1980

def decades(json_data):
    _decades_set = set((""))

    for json_object in json_data:
        _decades_set.add(json_object['year'])

    print(_decades_set)
    return _decades_set

def groupByDecade(json_data):
    dec1980 = []
    dec1990 = []
    dec2000 = []
    dec2010 = []
    dec2020 = []
    other = []
        
    for json_object in json_data:
        if type(json_object.year) != type(None):
            if 1980 <= json_object.year <= 1989:
                dec1980.append(json_object)
                    
            elif 1990 <= json_object.year <= 1999:
                dec1990.append(json_object)

            elif 2000 <= json_object.year <= 2009:
                dec2000.append(json_object)
                
            elif 2010 <= json_object.year <= 2019:
                dec2010.append(json_object)

            elif 2020 <= json_object.year <= 2029:
                dec2020.append(json_object)
            else:
                other.append(json_object)

    return dec1980 #, dec1990, dec2000, dec2010, dec2020, other
    #Perserves namespace information



def listPrinter(json_data):
    for game in json_data:
        print(game)


game_data = api.requests_NameSpace("https://api.dccresource.com/api/games")

eighties = groupByDecade(game_data)

listPrinter(eighties)


