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

    def test_percentage_home_wins(self):
        game_stats = GameStats()

        self.assertEqual(game_stats.percentage_home_wins(), 0.44)

    def test_percentage_visitor_wins(self):
        game_stats = GameStats()

        self.assertEqual(game_stats.percentage_visitor_wins(), 0.36)

    def test_percentage_ties(self):
        game_stats = GameStats()

        self.assertEqual(game_stats.percentage_ties(), 0.20)

    def test_count_of_games_by_season(self):
        game_stats = GameStats()
        expected = {
            "20122013": 806,
            "20162017": 1317,
            "20142015": 1319,
            "20152016": 1321,
            "20132014": 1323,
            "20172018": 1355
        }
        self.assertEqual(game_stats.count_of_games_by_season(), expected)

    def test_average_goals_per_game(self):
        game_stats = GameStats()

        self.assertEqual(game_stats.average_goals_per_game(), 4.22)

    def test_average_goals_by_season(self):
        game_stats = GameStats()
        expected = {
            "20122013": 4.12,
            "20162017": 4.23,
            "20142015": 4.14,
            "20152016": 4.16,
            "20132014": 4.19,
            "20172018": 4.44
        }

        self.assertEqual(game_stats.average_goals_by_season(), expected)
