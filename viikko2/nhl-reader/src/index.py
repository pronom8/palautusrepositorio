
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    perus_kaura_url = "https://studies.cs.helsinki.fi/nhlstats"
    

    season = input("Select season (e.g., 2018-19, 2019-20, etc.): ")
    nationality = input("Select nationality (e.g., FIN, SWE, CAN): ").upper()

    reader = PlayerReader(perus_kaura_url, season)
    stats = PlayerStats(reader)
    
   # players = stats.top_scorers_by_nationality("FIN")

    stats.top_scorers_by_nationality(nationality)



   # for player in players:
    #    print(player)
if __name__ == "__main__":
    main()
