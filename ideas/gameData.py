
import json
import requests

from types import SimpleNamespace

from collections import Counter as ct
import collections as col
    
def api_request(): #Handle errors gracefully
    response = requests.get("https://api.dccresource.com/api/games")
    json_data = json.loads(response.content, object_hook=lambda d:SimpleNamespace(**d))\
        if response and response.status_code == 200 else None
    return json_data


def find_Platforms(json_data):
    #finds unique publishers taking advantage of the set data structure
    
    #Constructor
    platform_set = set((""))
    
    for json_object in json_data:
        platform_set.add(json_object.platform)
   
    print(f"A list {platform_set}") 
    print(len(platform_set)) # 


def droplowest(platforms, min): #deletes publishers with less than min number
    for platform , titles in platforms.most_common():
        if titles < min:
            del platforms[platform]
    
    #Displays the list of publishers with less titles than min
    for platform, titles in platforms.most_common():
        print(platform, titles)
    print(len(platforms))
    
    return platforms


# Counts the number of publishers    
def count_Platform(json_data):
    
    platforms = ct(k.platform for k in json_data if k.platform)
    # for publisher, count in publishers.most_common():
        # print(publisher, count)
    return platforms


def top_Platforms(platforms, top): 
    top_platforms = set((""))
    top_platforms = dict(ct(platforms).most_common(top))
    #for publisher, count in publishers.most_common():

    print(top_platforms)
    print(len(top_platforms))

    return top_platforms


def split_Key(platforms): #ReturnsDict
    platform_names = platforms.keys()
    print(platform_names)
    return platform_names


def split_Values(platforms): #ReturnsDict
    platform_titles = platforms.values()
    #for platform in platform_titles:
    print(platform_titles)
    return platform_titles

def zip_Platforms(platforms):
    names , titles = zip(*platforms.items())
    print(names)
    print(titles)
    return names, titles
    
def group_PlatformManufacture(publishers, year): #Groups consoles by manufacturer
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
                else:
                    Other.append(publisher)


    return Nintendo, Sony, Atari, Microsoft, Atari, Sega, PerComp, Other

game_data = api_request()

find_Platforms(game_data)                       #find unique platforms
platforms = count_Platform(game_data)           #Counts titles per platform
topPlatforms = top_Platforms(platforms, 31)     #Sorts the data by top platform descending order

groupedPlatforms = group_PlatformManufacture(game_data, 2000)
#returns two separate strings in order of platform names and titles count
platform_names, platform_titles_count = zip_Platforms(topPlatforms)

"""
platform_names = split_Key(topPlatforms)
platform_titles = split_values(topPlatforms)
top_ten = droplowest(platforms, 10)
"""
