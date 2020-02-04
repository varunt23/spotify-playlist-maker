import requests


endpoint_url = "https://api.spotify.com/v1/recommendations?"

limit=10
market="US"
seed_genres="rap"
target_danceability=0.9
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'

#something to the hold the 

class Query:
    def __init__(self, limit, genres,target_danceability, market, url):
        self.limit = limit
        self.genres = genres
        self.target_danceability = target_danceability
        self.market = market
        self.url = "https://api.spotify.com/v1/recommendations?"
    def getQuery(self):
         return f'{self.url}limit={self.limit}&market={self.market}&seed_genres={self.genres}&target_danceability={self.danceability}'


def printTracks(json_response):
    for i in json_response['tracks']:
           # uris.append(i)
            print(f"\"{i['name']}\" by {i['artists'][0]['name']}")

def getReccomendations():
    response = requests.get( query , headers={"Content-Type":"application/json", "Authorization": "Bearer BQCkEm27UO5Jt6yMuqI2LuU38AkZnFgNjMDHDin7iCrHT_MNuDFHKSxDhIxGJDOlbLp4glxH7v52fFmhFkSG9Y0Cq7csmV8f9Gl-Nns2KeCbd3lYWpmfT-zUlICu2tdgGcnJLorcWsuBUiGClVadL1PKRnNLqdxy6nRp-CYFVZusw-l3N3j7lRwrfQCDrVB0dJgTteXEGCVh2Ukv34hM3_cGM4LcSKPu7BPria6t7pALFjeOtuUj3itzcOqh3vwPCQJWjE6hVvyuuVWa"})
    json_response = response.json()
    printTracks(json_response)


getReccomendations()
