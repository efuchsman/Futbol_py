import unittest
from libraries.team_stats import TeamStats
from libraries.league_stats import LeagueStats
from libraries.game_stats import GameStats


class TestTeamStats(unittest.TestCase):
    def test_constructor(self):
        team_stats = TeamStats()

        self.assertIsInstance(team_stats, TeamStats)
        self.assertIsInstance(team_stats.game_stats, GameStats)
        self.assertIsInstance(team_stats.league_stats, LeagueStats)
        self.assertEqual(len(team_stats.all_teams), 32)

    def test_team_info(self):
        team_stats = TeamStats()

        expected = {
            "team_id": "18",
            "franchise_id": "34",
            "team_name": "Minnesota United FC",
            "abbreviation": "MIN",
            "stadium": "Allianz Field",
            "link": "/api/v1/teams/18"
        }

        self.assertEqual(team_stats.team_info("18"), expected)

    def test_best_season(self):
        team_stats = TeamStats()

        self.assertEqual(team_stats.best_season("6"), "20132014")

    def test_worst_season(self):
        team_stats = TeamStats()

        self.assertEqual(team_stats.worst_season("6"), "20142015")

    def test_average_win_percentage(self):
        team_stats = TeamStats()

        self.assertEqual(team_stats.average_win_percentage("6"), 0.49)

    def test_most_goals(self):
        team_stats = TeamStats()

        self.assertEqual(team_stats.most_goals("18"), 7)
