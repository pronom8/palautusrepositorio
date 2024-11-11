from rich.table import Table
from rich.console import Console

class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        """Palauta pelaajat kansalaisuuden mukaan, pisteiden mukaan laskevassa järjestyksessä"""
        filtered_players = [player for player in self.players if player.nationality == nationality]

        
        sorted_players = sorted(filtered_players, key=lambda player: player.kaikki_pisteet(), reverse=True)

        table = Table(title=f"Top scorers of {nationality}")

        table.add_column("Name", justify="left", style="cyan", no_wrap=True)
        table.add_column("Team", style="magenta")
        table.add_column("Goals", style="green")
        table.add_column("Assists", style="green")
        table.add_column("Points", style="yellow")

        for player in sorted_players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.kaikki_pisteet()))

        console = Console()
        console.print(table)
    
