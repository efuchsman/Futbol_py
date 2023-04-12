import unittest
from libraries.season_stats import SeasonStats


class TestSeasonStats(unittest.TestCase):
    def test_winningest_coach(self):
        season_stats = SeasonStats()

        self.assertEqual(season_stats.winningest_coach(
            "20132014"), "Claude Julien")

        self.assertEqual(season_stats.winningest_coach(
            "20142015"), "Alain Vigneault")
