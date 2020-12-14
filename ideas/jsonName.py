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

def publisher_data(json_data):
    data = []
    sales_Total = 0.0
    titles_Published = 0

    # counts number of titles published by Nintendo
    # counts global sales by Nintendo
    for json_object in json_data:
        if json_object.publisher == "Nintendo":
            #data.append(json_object["globalSales"])
            titles_Published += 1
            sales_Total += json_object.globalSales
    print(f"\n Nintendo's has published {titles_Published} titles")       
    print(f"\n Nintendo's global sales: ${sales_Total}")       

def find_publisher(json_data):
    #finds unique publishers taking advantage of the set data structure
    
    #Constructor
    publisher_set = set((""))
    
    for json_object in json_data:
        publisher_set.add(json_object.publisher)
   
    print(f"A list {publisher_set}") 
    print(len(publisher_set)) # 579 publishers

# Counts the number of publishers    
def count_publisher(json_data):
    
    publishers = ct(k.publisher for k in json_data if k.publisher)
    for publisher, count in publishers.most_common():
        print(publisher, count)
    return publishers

def droplowest(publishers, min): #deletes publishers with less than min number
    for publisher , titles in publishers.most_common():
        if titles < min:
            del publishers[publisher]
    
    #Displays the list of publishers with less titles than min
    for publisher, titles in publishers.most_common():
        print(publisher, titles)
    print(len(publishers))
    
    return publishers

def top_publishers(publishers, top): #deletes publishers with less than min number
    top_ten = set((""))
    top_ten = dict(ct(publishers).most_common(top))
    #for publisher, count in publishers.most_common():

    print(top_ten)
    print(len(top_ten))

    return top_ten

"""
FUNCTIONS
"""

json_data = api_request()

#publisher_data(json_data)
#finds unique publishers taking advantage of the set data structure
#find_publisher(json_data)                      

# Counts the number of publishers returns a dict with 
# Publisher, number of titles Published
publishers = count_publisher(json_data)

"""
#drops publishers with less than 50 titles
top_50_publishers = droplowest(publishers, 50)

top_10_publishers = top_publishers(top_50_publishers, 10)



data_in_file = json.load(json_data, strict=False)
            # 4. Iterate over objects and print relevant fields
            for json_object in data_in_file:
                print("ttl: %s, desc: %s" % (json_object['title'],json_object['description']) )
"""