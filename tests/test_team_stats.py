import unittest
from libraries.team_stats import TeamStats
from libraries.league_stats import LeagueStats
from libraries.game_stats import GameStats
from collections import defaultdict


class TestTeamStats(unittest.TestCase):
    def test_constructor(self):
        team_stats = TeamStats()

        self.assertIsInstance(team_stats, TeamStats)
        self.assertIsInstance(team_stats.game_stats, GameStats)
        self.assertIsInstance(team_stats.league_stats, LeagueStats)
        self.assertEqual(len(team_stats.all_teams), 32)
