import requests
from player import Player

class PlayerReader:
    def __init__(self, perus_kaura_url, season):
        self.url = f"{perus_kaura_url}/{season}/players"

    def get_players(self):
        
        response = requests.get(self.url).json()
        return [Player(player_dict) for player_dict in response]