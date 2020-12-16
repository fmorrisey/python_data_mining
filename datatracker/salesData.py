from types import SimpleNamespace

from collections import Counter as ct
import collections as col


#names , titles = platformData.copiesPerPlatform(gameData)

class salesData(object):
    def __init__(self, game_data):
        self.game_data = game_data
   

    """\"\"\"sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        \"\"\"""sumary_line"""
    def decades(json_data):
        _decades_set = set((""))

        for json_object in json_data:
            _decades_set.add(json_object['year'])

        print(_decades_set)
        return _decades_set

    def groupByDecade(json_data, decade):
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

        """Decade Switch"""
        switcher {
            1980: 
                for json_object in json_data:
                if type(json_object.year) != type(None):
                    if 1980 <= json_object.year <= 1989:
                        dec1980.append(json_object)
                return dec1980,
           
            }
        func = switcher.get(json_data, lambda: "nothing")
        
        
        

    # def eightiesPrinter(json_data):
        
