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
