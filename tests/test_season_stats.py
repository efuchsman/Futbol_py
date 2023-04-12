import unittest
from libraries.season_stats import SeasonStats
from libraries.league_stats import LeagueStats
from libraries.game_stats import GameStats
from collections import defaultdict


class TestSeasonStats(unittest.TestCase):
    def test_constructor(self):
        season_stats = SeasonStats()

        self.assertIsInstance(season_stats, SeasonStats)
        self.assertIsInstance(season_stats.game_stats, GameStats)
        self.assertIsInstance(season_stats.league_stats, LeagueStats)

    def test_season_games(self):
        season_stats = SeasonStats()

        self.assertIsInstance(season_stats.season_games("20132014"), list)
        self.assertEqual(season_stats.season_games(
            "20132014")[0], '2013030161')

    def test_season_shots(self):
        season_stats = SeasonStats()
        expected = {'16': 0.3042362002567394, '19': 0.31129032258064515, '30': 0.30363036303630364, '21': 0.31484502446982054, '26': 0.28327228327228327, '24': 0.3347763347763348, '25': 0.30015082956259426, '23': 0.26655629139072845, '4': 0.292259083728278, '17': 0.28780487804878047, '29': 0.3003194888178914, '15': 0.2819614711033275, '20': 0.3166023166023166, '18': 0.2938053097345133, '6': 0.3064066852367688,
                    '8': 0.29685157421289354, '5': 0.30377906976744184, '2': 0.2947019867549669, '52': 0.29411764705882354, '14': 0.3076923076923077, '13': 0.2641509433962264, '28': 0.2739541160593792, '7': 0.2682445759368836, '10': 0.31307550644567217, '27': 0.28907563025210087, '1': 0.3060428849902534, '9': 0.2638888888888889, '22': 0.2980769230769231, '3': 0.27007299270072993, '12': 0.2733224222585925}

        self.assertIsInstance(
            season_stats.season_shots("20132014"), defaultdict)

        self.assertEqual(
            season_stats.season_shots("20132014"), expected)

    def test_season_tackles(self):
        season_stats = SeasonStats()
        expected = {'16': 1836, '19': 2087, '30': 1787, '21': 2223, '26': 3691, '24': 2515, '25': 1820, '23': 1710, '4': 2404, '17': 1783, '29': 2915, '15': 1904, '20': 1708, '18': 1611,
                    '6': 2441, '8': 2211, '5': 2510, '2': 2092, '52': 2313, '14': 1774, '13': 1860, '28': 1931, '7': 1992, '10': 2592, '27': 2173, '1': 1568, '9': 2351, '22': 1751, '3': 2675, '12': 1807}

        self.assertIsInstance(
            season_stats.season_tackles("20132014"), defaultdict)

        self.assertEqual(
            season_stats.season_tackles("20132014"), expected)

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

    def test_most_tackles(self):
        season_stats = SeasonStats()

        self.assertEqual(season_stats.most_tackles(
            "20132014"), "FC Cincinnati")

        self.assertEqual(season_stats.most_tackles(
            "20142015"), "Seattle Sounders FC")

    def test_least_tackles(self):
        season_stats = SeasonStats()

        self.assertEqual(season_stats.least_tackles(
            "20132014"), "Atlanta United")

        self.assertEqual(season_stats.least_tackles(
            "20142015"), "Orlando City SC")
