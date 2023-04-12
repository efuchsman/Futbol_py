import unittest
from libraries.season_stats import SeasonStats


class TestSeasonStats(unittest.TestCase):
    def test_winningest_coach(self):
        season_stats = SeasonStats()

        self.assertEqual(season_stats.winningest_coach(
            "20132014"), "Claude Julien")

        self.assertEqual(season_stats.winningest_coach(
            "20142015"), "Alain Vigneault")

    def test_worst_coach(self):
        season_stats = SeasonStats()

        self.assertEqual(season_stats.worst_coach(
            "20132014"), "Peter Laviolette")

        self.assertIn(season_stats.worst_coach(
            "20142015"), ["Craig MacTavish", "Ted Nolan"])

    def test_most_accurate_team(self):
        season_stats = SeasonStats()

        self.assertEqual(season_stats.most_accurate_team(
            "20132014"), "Real Salt Lake")

        self.assertEqual(season_stats.most_accurate_team(
            "20142015"), "Toronto FC")

    def test_least_accurate_team(self):
        season_stats = SeasonStats()

        self.assertEqual(season_stats.least_accurate_team(
            "20132014"), "New York City FC")

        self.assertEqual(season_stats.least_accurate_team(
            "20142015"), "Columbus Crew SC")
