import requests
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

def groupByDecade(json_data, **kwargs):
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
    if kwargs is not None:
        if kwargs == 1980:
            return dec1980
        elif kwargs == 1990:
            return dec1990
        elif kwargs == 2000:
            return dec2000
        elif kwargs == 2010:
            return dec2010
        elif kwargs == 2020:
            return dec2020
        elif kwargs == 'other' or kwargs == 'O':
            return other
        else: pass
    else : return dec1980, dec1990, dec2000, dec2010, dec2020, other
    
    #Perserves namespace information

def salesPerPlatformOLD(json_data, yearMin, yearMax):
    MicX360 = 0, MicXOne = 0, SonyPS2 = 0, SonyPS3 = 0, SonyPS4 = 0, SonyPSP = 0, SonyPSV = 0, SonyPSV = 0
    salesPer_Dict = {
        "X360":0, "XOne":0, ""
    }


    ('DS', 'PS2', 'PS3', 'Wii', 'X360', 'PSP', 'PS', 'PC', 'XB', 'GBA', 'GC')
    for title in json_data:
        if type(title.year) != type(None):
            if yearMin <= title.year <= yearMax:
                #Microsoft Platforms
                if title.platform == 'X360':
                    MicX360 += title.globalSales
                elif title.platform == 'XOne':
                    MicXOne += title.globalSales
                else: pass
                
                elif title.platform == 'XOne':
                    MicXOne += title.globalSales
                #Sony Platforms
                elif title.platform == 'PS':
                    SonyPS2 += title.globalSales
                elif title.platform == 'PS2':
                    SonyPS2 += title.globalSales
                elif title.platform == 'PS3':
                    SonyPS3 += title.globalSales
                elif title.platform == 'PS4':
                    SonyPS4 += title.globalSales
                elif title.platform == 'PSP':
                    SonyPSP += title.globalSales
                elif title.platform == 'PSV':
                    SonyPSV += title.globalSales
                
        else: pass 

def copiesPer_Dict(game_data):   #Calls multiple functions to return two serpate lists of copies per console
        numberOfPlatforms = platformData._findUniquePlatforms(game_data, 2013, 2021)
        platforms = platformData._titlesPer(game_data)
        topPlatforms = platformData._top_Platforms(platforms, numberOfPlatforms)     #Sorts the data by top platform descending order
        return topPlatforms #Returns Dict


    def copiesPer_Lists(game_data):   #Calls multiple functions to return two serpate lists of copies per console
        numberOfPlatforms = platformData._findUniquePlatforms(game_data, 2013, 2021)
        platforms = platformData._titlesPer(game_data)
        topPlatforms = platformData._top_Platforms(platforms, numberOfPlatforms)     #Sorts the data by top platform descending order
        platform_names, platform_titles_count = platformData._zip_Platforms(topPlatforms) #Pulls the dictionary apart
        return platform_names, platform_titles_count #Return Lists
    
    def salesPer_Dict(game_data):   #Calls multiple functions to return two serpate lists of copies per console
        salesPerPlatform = platformData.
        return salesPerPlatform #Returns Dict

    
    # Counts the number of platforms    
    def _titlesPer(json_data):
        platforms = ct(k.platform for k in json_data if k.platform)
        return platforms
"""






"""
def findUniquePublishers(json_data, yearMin, yearMax):
        #finds unique publishers taking advantage of the set data structure
        #Constructor
        publisher_set = set((""))
        
        for json_object in json_data:
            if yearMin <= json_object.year <= yearMax:
                publisher_set.add(json_object.publisher)

        unique_platforms = len(publisher_set)
        return unique_platforms


def platformOverDecade(json_data, platform):

    for decade in json_data:
        for platform in decade:
            break
    
    return null
            

def NintendoAfter(gameData, year):
        NintendoGames = _groupManufactures(gameData, year)
        return NintendoGames


def _groupManufactures(publishers, year): #Groups consoles by manufacturer
        Nintendo = []
        Sony = []
        Microsoft = []
        Atari = []
        Sega = []
        PerComp = []
        Other = []
        
        for publisher in publishers:
            if type(publisher.year) != type(None):
                if publisher.year >= year:
                    if (publisher.platform == 'NES') or (publisher.platform == 'GC') or (publisher.platform == 'SNES') or (publisher.platform == 'GBA') or (publisher.platform == 'GB') or (publisher.platform == 'Wii') or (publisher.platform == 'WiiU') or (publisher.platform == 'DS') or (publisher.platform == '3DS') or (publisher.platform == 'N64'):
                        Nintendo.append(publisher)
                    else:
                        Other.append(publisher)
                    
                    elif (publisher.platform == 'XB') or (publisher.platform == 'XOne') or (publisher.platform == 'X360'):
                        Microsoft.append(publisher)
                    elif (publisher.platform == 'PS') or (publisher.platform == 'PS2') or (publisher.platform == 'PS3') or (publisher.platform == 'PSP') or (publisher.platform == 'PS4') or (publisher.platform == 'PSV') or (publisher.platform == 'PSV'):
                        Sony.append(publisher)
                    elif (publisher.platform == 'SAT') or (publisher.platform == 'GEN'):
                        Sega.append(publisher)
                    elif (publisher.platform == '2600'):
                        Atari.append(publisher)
                    elif (publisher.platform == 'PC'):
                        PerComp.append(publisher)
                    
                else:pass
            else: pass

        return Nintendo #, Sony, Atari, Microsoft, Atari, Sega, PerComp, Other

"""

def listPrinter(json_data):
    for game in json_data:
        print(game)

def requests_NameSpace(apiUrl): #Handle errors gracefully
        response = requests.get(apiUrl)
        json_data = json.loads(response.content, object_hook=lambda d:SimpleNamespace(**d))\
            if response and response.status_code == 200 else None
        print(type(json_data))
        return json_data

game_data = requests_NameSpace("https://api.dccresource.com/api/games")

#eighties = groupByDecade(game_data, 1980)

salesPer = _salesPer_Dict(game_data, 2013, 2021)

listPrinter(salesPer)


