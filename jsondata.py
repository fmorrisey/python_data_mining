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
    
    #Constructor
    publisher_set = set((""))
    
    for json_object in json_data:
        publisher_set.add(json_object["publisher"])
                
    
    print(publisher_set) 
    print(len(publisher_set)) # 579 publishers
    
def count_publisher(json_data):
    return null

# publisher_data()


find_publisher(api_request())




"""
data_in_file = json.load(json_data, strict=False)
            # 4. Iterate over objects and print relevant fields
            for json_object in data_in_file:
                print("ttl: %s, desc: %s" % (json_object['title'],json_object['description']) )
"""