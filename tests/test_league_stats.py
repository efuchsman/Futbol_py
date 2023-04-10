import unittest
from libraries.league_stats import LeagueStats


class TestLeagueStats(unittest.TestCase):
    def test_constructor(self):
        league_stats = LeagueStats()

        self.assertIsInstance(league_stats, LeagueStats)
        self.assertIsInstance(league_stats.all_game_teams, list)
        self.assertEqual(len(league_stats.all_game_teams), 14882)

        self.assertIsInstance(league_stats.all_teams, list)

    def test_count_of_teams(self):
        league_stats = LeagueStats()

        self.assertEqual(league_stats.count_of_teams(), 32)

    def test_best_offense(self):

        league_stats = LeagueStats()

        self.assertEqual(league_stats.best_offense(), "Reign FC")
