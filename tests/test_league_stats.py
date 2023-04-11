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

    def test_worst_offense(self):
        league_stats = LeagueStats()

        self.assertEqual(league_stats.worst_offense(), "Utah Royals FC")

    def test_highest_scoring_visitor(self):
        league_stats = LeagueStats()

        self.assertEqual(
            league_stats.highest_scoring_visitor(), "FC Dallas")

    def test_highest_scoring_home_team(self):
        league_stats = LeagueStats()

        self.assertEqual(
            league_stats.highest_scoring_home_team(), "Reign FC")

    def test_lowest_scoring_visitor(self):
        league_stats = LeagueStats()

        self.assertEqual(
            league_stats.lowest_scoring_visitor(), "San Jose Earthquakes")

    def test_lowest_scoring_home_team(self):
        league_stats = LeagueStats()

        self.assertEqual(
            league_stats.lowest_scoring_home_team(), "Utah Royals FC")
