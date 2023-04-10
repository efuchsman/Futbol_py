import unittest
from libraries.game_stats import GameStats


class TestGameStats(unittest.TestCase):
    def test_constructor(self):

        game_stats = GameStats()

        self.assertIsInstance(game_stats, GameStats)
        self.assertIsInstance(game_stats.all_games, list)
        self.assertEqual(len(game_stats.all_games), 7441)

    def test_highest_total_score(self):

        game_stats = GameStats()

        self.assertEqual(game_stats.highest_total_score(), 11)

    def test_lowest_total_score(self):

        game_stats = GameStats()

        self.assertEqual(game_stats.lowest_total_score(), 0)
