#from platformData import platformData as pfd
from api import api
from salesData import salesData as sds
from printer import printer as pt

if __name__ == '__main__':    
    
    # Use this line for external API Requests
    #game_data = api.requests_NameSpace("https://api.dccresource.com/api/games")
    
    # Use this line to open local data
    game_data = api.request_local('response.json')
    
    salesdata = sds.salesPer_Regional(game_data, 2013, 2021)
    pt.dict(salesdata)
