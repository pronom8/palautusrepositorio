import unittest
from statistics_service import StatisticsService
from player import Player


class StubPlayerReader:
    def get_players(self):
        
        return [
            Player("Wayne Gretzky", "EDM", 894, 1963),
            Player("Mario Lemieux", "PIT", 690, 1723),
            Player("Jaromir Jagr", "PIT", 766, 1921),
            Player("Mark Messier", "EDM", 694, 1887),
            Player("Paul Coffey", "EDM", 396, 1531),
            Player("Bobby Orr", "BOS", 270, 915),
            Player("Sidney Crosby", "PIT", 550, 1500),
            Player("Alex Ovechkin", "WSH", 730, 1390),
            Player("Connor McDavid", "EDM", 251, 850),
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        
        reader_stub = StubPlayerReader()
        self.statistics = StatisticsService(reader_stub)

    def test_search_finds_existing_player(self):
        player = self.statistics.search("Wayne Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Wayne Gretzky")

    def test_search_returns_none_for_nonexistent_player(self):
        player = self.statistics.search("Nonexistent Player")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        team_players = self.statistics.team("EDM")
        team_names = [player.name for player in team_players]
        self.assertIn("Wayne Gretzky", team_names)
        self.assertIn("Mark Messier", team_names)
        self.assertIn("Paul Coffey", team_names)
        self.assertEqual(len(team_players), 4)  

    def test_top_returns_correct_number_of_players(self):
        top_players = self.statistics.top(3)
        self.assertEqual(len(top_players), 3)

    def test_top_returns_players_sorted_by_points(self):
        top_players = self.statistics.top(3)
        self.assertEqual(top_players[0].name, "Wayne Gretzky")
        self.assertEqual(top_players[1].name, "Mario Lemieux")
        self.assertEqual(top_players[2].name, "Jaromir Jagr")