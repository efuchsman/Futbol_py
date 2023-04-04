import csv
import os
from libraries.csv_loader import CsvLoader
import pdb


class Gamestats(CsvLoader):

    def highest_total_score(self):
        max_score = 0
        for row in self.all_games:
            total_score = int(row['away_goals']) + int(row['home_goals'])
            max_score = max(max_score, total_score)
        return max_score
