
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    lukija = PlayerReader(url)
    stats = PlayerStats(lukija)
    
    players = stats.top_scorers_by_nationality("FIN")


    for player in players:
        print(player)
if __name__ == "__main__":
    main()
