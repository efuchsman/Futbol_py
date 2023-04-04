import unittest
import csv
import os
from libraries.csv_loader import CsvLoader


class TestCsvLoader(unittest.TestCase):
    def test_constructor(self):
        csvs = {
            'games_csv': csv.DictReader(open('./data/games.csv')),
            'game_teams_csv': csv.DictReader(open('./data/game_teams.csv')),
            'teams_csv': csv.DictReader(open('./data/teams.csv'))
        }
        csv_loader = CsvLoader(csvs)

        self.assertIsInstance(csv_loader, CsvLoader)
        self.assertIsInstance(csv_loader.all_teams, list)
        self.assertIsInstance(csv_loader.all_games, list)
        self.assertIsInstance(csv_loader.all_game_teams, list)
        self.assertEqual(len(csv_loader.all_teams), 32)
        self.assertEqual(len(csv_loader.all_games), 7441)
        self.assertEqual(len(csv_loader.all_game_teams), 14882)
