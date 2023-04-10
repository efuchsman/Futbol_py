import csv


class GameStats():
    def __init__(self):
        file = {'games_csv': csv.DictReader(open('./data/games.csv'))}
        self.all_games = []

        for row in file['games_csv']:
            self.all_games.append(row)

    def highest_total_score(self):
        max_score = 0
        for row in self.all_games:
            total_score = int(row['away_goals']) + int(row['home_goals'])
            max_score = max(max_score, total_score)
        return max_score

    def lowest_total_score(self):
        min_score = 5
        for row in self.all_games:
            total_score = int(row['away_goals']) + int(row['home_goals'])
            min_score = min(min_score, total_score)
        return min_score
