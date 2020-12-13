import json
import requests

from time import sleep
from progress.spinner import MoonSpinner

def data():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    json_data = response.json() if response and response.status_code == 200 else None
    data = []

    for json_object in json_data:
        print("id: %s" % (json_object["id"]))
        print("name: %s" % (json_object["name"]))

        data.append(json_object["id"])
        data.append(json_object["name"])
        data.append(json_object["email"])

    print(data)


def publisher_data():
    data = []
    sales_Total = 0.0
    titles_Published = 0

    response = requests.get("https://api.dccresource.com/api/games")
    json_data = response.json() if response and response.status_code == 200 else None
    
    bar = MoonSpinner('Processing...', max = len(json_data))

        #print("publisher: %s" % (json_object["publisher"]))

    for json_object in json_data:
        if json_object["publisher"] == "Nintendo":
            #data.append(json_object["globalSales"])
            titles_Published += 1
            sales_Total += json_object["globalSales"]
           
    bar.next()
    sleep(0.02)

    print(f"\n Nintendo's has published {titles_Published} titles")       
    print(f"\n Nintendo's global sales: ${sales_Total}")       

def find_publisher():
    response = requests.get("https://api.dccresource.com/api/games")
    json_data = response.json() if response and response.status_code == 200 else None
    
    publisher_set = set(("Publishers"))

    for json_object in json_data:
        publisher_set.add(json_object["publisher"])
    
    print(publisher_set)


# publisher_data()

find_publisher()




"""
data_in_file = json.load(json_data, strict=False)
            # 4. Iterate over objects and print relevant fields
            for json_object in data_in_file:
                print("ttl: %s, desc: %s" % (json_object['title'],json_object['description']) )
"""