
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
    
    

def group_consoleManufacture(publishers, top): #deletes publishers with less than min number
    top_ten = set((""))

    top_ten = dict(ct(publishers).most_common(top))
    #for publisher, count in publishers.most_common():

    print(top_ten)
    print(len(top_ten))

    return top_ten

game_data = api_request()

find_Platforms(game_data)                       #find unique platforms
platforms = count_Platform(game_data)           #Counts titles per platform
topPlatforms = top_Platforms(platforms, 25)     #Sorts the data by top platform descending order

#returns two separate strings in order of platform names and titles count
platform_names, platform_titles_count = zip_Platforms(topPlatforms)

"""
platform_names = split_Key(topPlatforms)
platform_titles = split_values(topPlatforms)
top_ten = droplowest(platforms, 10)
"""
