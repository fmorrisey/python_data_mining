from platformData import platformData as pfd
from api import api
from salesData import salesData as sds

if __name__ == '__main__':
    game_data = api.requests_NameSpace("https://api.dccresource.com/api/games")
    salesPer = pfd.salesPer_Dict(game_data)
    print(salesPer)
    
    