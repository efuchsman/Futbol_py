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

    def best_offense(self):
        teams_hash = defaultdict(str)
        team_goals_hash = defaultdict(int)
        team_game_count_hash = defaultdict(int)
        avg_goals_game_hash = defaultdict(int)

        for team in self.all_teams:
            teams_hash[team['team_id']] += team['teamName']

        for game in self.all_game_teams:
            team_goals_hash[teams_hash[game['team_id']]] += int(game['goals'])
            team_game_count_hash[teams_hash[game['team_id']]] += 1

        for team in team_goals_hash:
            avg_goals_game_hash[team] += round(
                (float(team_goals_hash[team])/float(team_game_count_hash[team])), 2)

        best_avg = 0

        for team in avg_goals_game_hash:
            best_avg = max(best_avg, avg_goals_game_hash[team])

        for team in avg_goals_game_hash:
            if avg_goals_game_hash[team] == best_avg:
                return team
