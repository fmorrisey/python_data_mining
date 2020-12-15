from types import SimpleNamespace

from collections import Counter as ct
import collections as col


#names , titles = platformData.copiesPerPlatform(gameData)

class salesData(object):
    def __init__(self, game_data):
        self.game_data = game_data

    def byConsolePerDecade(game_data):
        #years = salesData.decades(game_data)
        dec1980 = salesData.groupByDecade(game_data)
        eightiesPrinter(dec1980)
        pass

        return dec1980

    def decades(json_data):
        _decades_set = set((""))

        for json_object in json_data:
            _decades_set.add(json_object['year'])

        print(_decades_set)
        return _decades_set

    def groupByDecade(json_data):
        dec1980 = {}
        dec1990 = {}
        dec2000 = {}
        dec2010 = {}
        dec2020 = {}
        other = {}
         
        for json_object in json_data:
            if type(json_object.year) != type(None):
                if 1980 <= json_object.year >= 1990:
                    dec1980 = dec1980 | json_object
                       
                elif 1990 <= json_object.year <= 1999:
                    dec1990 = dec1990 | json_object

                elif 2000 <= json_object.year <= 2009:
                    dec2000 = dec2000 | json_object
                    
                elif 2010 <= json_object.year <= 2019:
                    dec2010 = dec2010 | json_object

                elif 2020 <= json_object.year <= 2021:
                    dec2020 = dec2020 | json_object

        return dec1980 , dec1990, dec2000, dec2010, dec2020, other

    #def eightiesPrinter(json_data):
        
