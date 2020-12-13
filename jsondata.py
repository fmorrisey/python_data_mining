import json
import requests as rp
from collections import Counter as ct

from time import sleep
from progress.spinner import MoonSpinner

def data():
    json_data = dict()
    response = rp.get("https://jsonplaceholder.typicode.com/users")
    json_data = response.json() if response and response.status_code == 200 else None
    data = []

    for json_object in json_data:
        print("id: %s" % (json_object["id"]))
        print("name: %s" % (json_object["name"]))

        data.append(json_object["id"])
        data.append(json_object["name"])
        data.append(json_object["email"])

    print(data)

def api_request():
    response = rp.get("https://api.dccresource.com/api/games")
    json_data = response.json() if response and response.status_code == 200 else None
    return json_data

def publisher_data(json_data):
    data = []
    sales_Total = 0.0
    titles_Published = 0
    
    bar = MoonSpinner('Processing...', max = len(json_data))

        #print("publisher: %s" % (json_object["publisher"]))

    # counts number of titles published by Nintendo
    # counts global sales by Nintendo
    for json_object in json_data:
        if json_object["publisher"] == "Nintendo":
            #data.append(json_object["globalSales"])
            titles_Published += 1
            sales_Total += json_object["globalSales"]
    
    # Moonspinner cause why not?           
    bar.next()
    sleep(0.02)

    print(f"\n Nintendo's has published {titles_Published} titles")       
    print(f"\n Nintendo's global sales: ${sales_Total}")       

def find_publisher(json_data):
    #finds unique publishers taking advantage of the set data structure
    #Constructor
    publisher_set = set((""))
    
    for json_object in json_data:
        publisher_set.add(json_object["publisher"])
                
    
    print(publisher_set) 
    print(len(publisher_set)) # 579 publishers

# Counts the number of publishers    
def count_publisher(json_data):
    
    publishers = ct(k['publisher'] for k in json_data if k.get('publisher'))
    # for publisher, count in publishers.most_common():
        # print(publisher, count)
    return publishers

def droplowest(publishers, min): #deletes publishers with less than min number
    for publisher , count in publishers.most_common():
        if count < min:
            del publishers[publisher]

    for publisher, count in publishers.most_common():
        print(publisher, count)

    print(len(publishers))



# publisher_data()

json_data = api_request()
#find_publisher(json_data)
publishers = count_publisher(json_data)
top_publishers = droplowest(publishers, 50)





"""
data_in_file = json.load(json_data, strict=False)
            # 4. Iterate over objects and print relevant fields
            for json_object in data_in_file:
                print("ttl: %s, desc: %s" % (json_object['title'],json_object['description']) )
"""