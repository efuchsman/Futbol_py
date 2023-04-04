import unittest
import csv
import os
from libraries.csv_loader import CsvLoader


class TestCsvLoader(unittest.TestCase):
    def test_constructor(self):
        directory = './data'
        files = {
            'games_csv': csv.DictReader(open(os.path.join(directory, 'games.csv'))),
            'game_teams_csv': csv.DictReader(open(os.path.join(directory, 'game_teams.csv'))),
            'teams_csv': csv.DictReader(open(os.path.join(directory, 'teams.csv')))
        }
        csv_loader = CsvLoader(files)

        self.assertIsInstance(csv_loader, CsvLoader)
