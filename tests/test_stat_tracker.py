import unittest
from libraries.team_stats import TeamStats
from libraries.league_stats import LeagueStats
from libraries.game_stats import GameStats
from libraries.season_stats import SeasonStats
from libraries.stat_tracker import StatTracker


class TestStatTracker(unittest.TestCase):
    def test_constructor(self):
        stat_tracker = StatTracker()

        self.assertIsInstance(stat_tracker, StatTracker)
        self.assertIsInstance(stat_tracker.league_stats, LeagueStats)
        self.assertIsInstance(stat_tracker.game_stats, GameStats)
        self.assertIsInstance(stat_tracker.team_stats, TeamStats)
        self.assertIsInstance(stat_tracker.season_stats, SeasonStats)

        self.assertEqual(stat_tracker.highest_total_score, 11)
        self.assertEqual(stat_tracker.lowest_total_score, 0)
        self.assertEqual(stat_tracker.percentage_home_wins, 0.44)
        self.assertEqual(stat_tracker.percentage_visitor_wins, 0.36)
        self.assertEqual(stat_tracker.percentage_ties, 0.20)
        self.assertEqual(stat_tracker.highest_total_score, 11)

        expected_count_of_games_by_season = {
            "20122013": 806,
            "20162017": 1317,
            "20142015": 1319,
            "20152016": 1321,
            "20132014": 1323,
            "20172018": 1355
        }

        self.assertEqual(stat_tracker.count_of_games_by_season,
                         expected_count_of_games_by_season)
        self.assertEqual(stat_tracker.average_goals_per_game, 4.22)

        expected_average_goals_by_season = {
            "20122013": 4.12,
            "20162017": 4.23,
            "20142015": 4.14,
            "20152016": 4.16,
            "20132014": 4.19,
            "20172018": 4.44
        }

        self.assertEqual(stat_tracker.average_goals_by_season,
                         expected_average_goals_by_season)
        self.assertEqual(stat_tracker.count_of_teams, 32)
        self.assertEqual(stat_tracker.best_offense, "Reign FC")
        self.assertEqual(stat_tracker.worst_offense, "Utah Royals FC")
        self.assertEqual(stat_tracker.highest_scoring_visitor, "FC Dallas")
        self.assertEqual(stat_tracker.highest_scoring_home_team, "Reign FC")
        self.assertEqual(stat_tracker.lowest_scoring_visitor,
                         "San Jose Earthquakes")
