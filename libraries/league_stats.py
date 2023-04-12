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
        self.teams_hash = defaultdict(str)
        self.team_goals_hash = defaultdict(int)
        self.team_game_count_hash = defaultdict(int)
        self.avg_goals_game_hash = defaultdict(int)

        for row in game_teams_file['game_teams_csv']:
            self.all_game_teams.append(row)

        for row in teams_file['teams_csv']:
            self.all_teams.append(row)

        for team in self.all_teams:
            self.teams_hash[team['team_id']] += team['teamName']

    def count_of_teams(self):
        return len(self.all_teams)

    def best_offense(self):

        for game in self.all_game_teams:
            self.team_goals_hash[self.teams_hash[game['team_id']]
                                 ] += int(game['goals'])
            self.team_game_count_hash[self.teams_hash[game['team_id']]] += 1

        for team in self.team_goals_hash:
            self.avg_goals_game_hash[team] += round(
                (float(self.team_goals_hash[team])/float(self.team_game_count_hash[team])), 2)

        best_avg = 0

        for team in self.avg_goals_game_hash:
            best_avg = max(best_avg, self.avg_goals_game_hash[team])

        for team in self.avg_goals_game_hash:
            if self.avg_goals_game_hash[team] == best_avg:
                return team

    def worst_offense(self):

        for game in self.all_game_teams:
            self.team_goals_hash[self.teams_hash[game['team_id']]
                                 ] += int(game['goals'])
            self.team_game_count_hash[self.teams_hash[game['team_id']]] += 1

        for team in self.team_goals_hash:
            self.avg_goals_game_hash[team] += round(
                (float(self.team_goals_hash[team])/float(self.team_game_count_hash[team])), 2)

        worst_avg = 5

        for team in self.avg_goals_game_hash:
            worst_avg = min(worst_avg, self.avg_goals_game_hash[team])

        for team in self.avg_goals_game_hash:
            if self.avg_goals_game_hash[team] == worst_avg:
                return team

    def highest_scoring_visitor(self):
        visitor_goals_hash = defaultdict(int)

        for game in self.all_game_teams:
            if game['HoA'] == "away":
                visitor_goals_hash[game['team_id']] += int(game['goals'])
                self.team_game_count_hash[game['team_id']] += 1

        for team in visitor_goals_hash:
            self.avg_goals_game_hash[team] += round(
                (float(visitor_goals_hash[team])/float(self.team_game_count_hash[team])), 2)

        best_avg = 0

        for team in self.avg_goals_game_hash:
            best_avg = max(best_avg, self.avg_goals_game_hash[team])

        for team in self.avg_goals_game_hash:
            if self.avg_goals_game_hash[team] == best_avg:
                return self.teams_hash[team]

    def highest_scoring_home_team(self):
        home_goals_hash = defaultdict(int)

        for game in self.all_game_teams:
            if game['HoA'] == "home":
                home_goals_hash[game['team_id']] += int(game['goals'])
                self.team_game_count_hash[game['team_id']] += 1

        for team in home_goals_hash:
            self.avg_goals_game_hash[team] += round(
                (float(home_goals_hash[team])/float(self.team_game_count_hash[team])), 2)

        best_avg = 0

        for team in self.avg_goals_game_hash:
            best_avg = max(best_avg, self.avg_goals_game_hash[team])

        for team in self.avg_goals_game_hash:
            if self.avg_goals_game_hash[team] == best_avg:
                return self.teams_hash[team]

    def lowest_scoring_visitor(self):
        visitor_goals_hash = defaultdict(int)

        for game in self.all_game_teams:
            if game['HoA'] == "away":
                visitor_goals_hash[game['team_id']] += int(game['goals'])
                self.team_game_count_hash[game['team_id']] += 1

        for team in visitor_goals_hash:
            self.avg_goals_game_hash[team] += round(
                (float(visitor_goals_hash[team])/float(self.team_game_count_hash[team])), 2)

        lowest_avg = 100

        for team in self.avg_goals_game_hash:
            lowest_avg = min(lowest_avg, self.avg_goals_game_hash[team])

        for team in self.avg_goals_game_hash:
            if self.avg_goals_game_hash[team] == lowest_avg:
                return self.teams_hash[team]

    def lowest_scoring_home_team(self):
        visitor_goals_hash = defaultdict(int)

        for game in self.all_game_teams:
            if game['HoA'] == "home":
                visitor_goals_hash[game['team_id']] += int(game['goals'])
                self.team_game_count_hash[game['team_id']] += 1

        for team in visitor_goals_hash:
            self.avg_goals_game_hash[team] += round(
                (float(visitor_goals_hash[team])/float(self.team_game_count_hash[team])), 2)

        lowest_avg = 100

        for team in self.avg_goals_game_hash:
            lowest_avg = min(lowest_avg, self.avg_goals_game_hash[team])

        for team in self.avg_goals_game_hash:
            if self.avg_goals_game_hash[team] == lowest_avg:
                return self.teams_hash[team]
