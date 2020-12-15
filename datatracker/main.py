from platformData import platformData as pfd
from api import api
from salesData import salesData as sds

if __name__ == '__main__':
    game_data = api.requests_JSONDict("https://api.dccresource.com/api/games")
    #copiesPer = pfd.copiesPer(game_data)
    
    dec1980 = sds.decadesGrouping(game_data)
    
    