from platformData import platformData as pfd
from api import api

if __name__ == '__main__':
    gameData = api.requests_NameSpace("https://api.dccresource.com/api/games")
    copiesPer = pfd.copiesPer(gameData)

    info = pfd._titlesPer(gameData)

