import csv
import pdb
import os


class CsvLoader:
    def __init__(self, csvs):
        self.all_teams = []
        self.all_games = []
        self.all_game_teams = []

        for row in csvs['games_csv']:
            self.all_games.append(row)

        for row in csvs['game_teams_csv']:
            self.all_game_teams.append(row)

        for row in csvs['teams_csv']:
            self.all_teams.append(row)

    @classmethod
    def from_csv_directory(cls, directory):
        files = {
            'games_csv': csv.DictReader(open(os.path.join(directory, 'games.csv'))),
            'game_teams_csv': csv.DictReader(open(os.path.join(directory, 'game_teams.csv'))),
            'teams_csv': csv.DictReader(open(os.path.join(directory, 'teams.csv')))
        }
        return cls(files)
