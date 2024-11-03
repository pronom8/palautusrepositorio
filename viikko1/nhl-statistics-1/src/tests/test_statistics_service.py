import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Gretzky")

    def test_search_returns_none_if_player_not_found(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)  
        self.assertEqual(team_players[0].name, "Semenko")
        self.assertEqual(team_players[1].name, "Kurri")
        self.assertEqual(team_players[2].name, "Gretzky")

    def test_top_returns_top_players(self):
        top_players = self.stats.top(2)  
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  
        self.assertEqual(top_players[1].name, "Lemieux")  
        self.assertEqual(top_players[2].name, "Yzerman") 

    def test_top_does_not_fail_with_zero(self):
        top_players = self.stats.top(0)
        self.assertEqual(len(top_players), 1)  
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_top_does_not_fail_if_how_many_is_greater_than_list_size(self):
        top_players = self.stats.top(10)  
        self.assertEqual(len(top_players), 5)

