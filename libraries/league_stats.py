import csv
from collections import defaultdict
import pdb


class LeagueStats():
    def __init__(self):
        game_teams_file = {'game_teams_csv': csv.DictReader(
            open('./data/game_teams.csv'))}
        teams_file = {'teams_csv': csv.DictReader(
            open('./data/teams.csv'))}

        self.all_game_teams = []
        self.all_teams = []

        for row in game_teams_file['game_teams_csv']:
            self.all_game_teams.append(row)

        for row in teams_file['teams_csv']:
            self.all_teams.append(row)

    def count_of_teams(self):
        return len(self.all_teams)
