from types import SimpleNamespace

from collections import Counter as ct
import collections as col

from requests import NullHandler

#names , titles = platformData.copiesPerPlatform(gameData)

class salesData(object):
    def __init__(self, game_data):
        self.game_data = game_data

    def byConsolePerDecade(game_data):
        #years = salesData.decades(game_data)
        dec1980 = salesData.decadesGrouping(game_data)
        pass

        return dec1980

    def decades(json_data):
        _decades_set = set((""))

        for json_object in json_data:
            _decades_set.add(json_object['year'])

        print(_decades_set)
        return _decades_set

    def decadesGrouping(json_data):
        dec1980 = dict()
        other = dict()
         
        for json_object in json_data:
            if json_object.year is None:
                pass
            elif json_object.year >= 1990:
                dec1980 = dict(json_object).update()
            else:
                other = dict(json_object).update()
                          
            """                
            elif 1990 <= json_object.year <= 1999:
                dec1990.update(json_object)
            elif 2000 <= json_object.year <= 2009:
                dec1990.update(json_object)
            elif 2010 <= json_object.year <= 2019:
                dec1990.update(json_object)
            elif 2020 <= json_object.year <= 2021:
                dec1990.update(json_object)
        return dec1980 , dec1990, dec2000, dec2010, dec2020, na
            """
        print(dec1980)
   