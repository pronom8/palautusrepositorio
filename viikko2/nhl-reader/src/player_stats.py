class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        """Palauta pelaajat kansalaisuuden mukaan, pisteiden mukaan laskevassa järjestyksessä"""
        filtered_players = [player for player in self.players if player.nationality == nationality]
        return sorted(filtered_players, key=lambda player: player.kaikki_pisteet(), reverse=True)