from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn
from week6t1 import All, Not, HasFewerThan, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)
    matcher = And(
    HasAtLeast(70, "points"),
    Or(
        PlaysIn("NYR"),
        PlaysIn("FLA"),
        PlaysIn("BOS")
    )
)

   #   matcher = And(
  #      HasAtLeast(5, "goals"),
   #     HasAtLeast(20, "assists"),
    #    PlaysIn("PHI")
    #)
    

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
