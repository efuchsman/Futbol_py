from collections import defaultdict
from .league_stats import LeagueStats
from .game_stats import GameStats


class TeamStats(GameStats, LeagueStats):
    def __init__(self):
        self.game_stats = GameStats()
        self.league_stats = LeagueStats()
        self.all_teams = self.league_stats.all_teams
        self.all_game_teams = self.league_stats.all_game_teams
        self.all_games = self.game_stats.all_games

    def team_info(self, id):
        team_hash = defaultdict(str)

        for team in self.all_teams:
            if team['team_id'] == id:
                team_hash['team_id'] += team['team_id']
                team_hash['franchise_id'] += team['franchiseId']
                team_hash['team_name'] += team['teamName']
                team_hash['abbreviation'] += team['abbreviation']
                team_hash['stadium'] += team['Stadium']
                team_hash['link'] += team['link']
        return team_hash

    def best_season(self, id):
        season_wins_hash = defaultdict(int)
        season_total_games_hash = defaultdict(int)
        season_win_percentage_hash = defaultdict(float)

        for game in self.all_game_teams:
            for season in self.all_games:
                if game['team_id'] == id and game['game_id'] == season['game_id']:
                    season_total_games_hash[season['season']] += 1
                    if game['result'] == "WIN":
                        season_wins_hash[season['season']] += 1

        for season in season_wins_hash:
            season_win_percentage_hash[season] += float(
                season_wins_hash[season]) / float(season_total_games_hash[season])

        best_season = 0

        for season in season_win_percentage_hash:
            best_season = max(best_season, season_win_percentage_hash[season])

        for season in season_win_percentage_hash:
            if season_win_percentage_hash[season] == best_season:
                return season

    def worst_season(self, id):
        season_win_hash = defaultdict(int)
        season_total_games_hash = defaultdict(int)
        season_win_percentage_hash = defaultdict(float)

        for game in self.all_game_teams:
            for season in self.all_games:
                if game['team_id'] == id and game['game_id'] == season['game_id']:
                    season_total_games_hash[season['season']] += 1
                    if game['result'] == "WIN":
                        season_win_hash[season['season']] += 1

        for season in season_win_hash:
            season_win_percentage_hash[season] += float(
                season_win_hash[season]) / float(season_total_games_hash[season])

        worst_season = 1.0

        for season in season_win_percentage_hash:
            worst_season = min(
                worst_season, season_win_percentage_hash[season])

        for season in season_win_percentage_hash:
            if season_win_percentage_hash[season] == worst_season:
                return season

    def average_win_percentage(self, id):
        total_wins = 0
        total_games = 0

        for game in self.all_game_teams:
            if game['team_id'] == id:
                total_games += 1
                if game['result'] == "WIN":
                    total_wins += 1
        return round((float(total_wins) / float(total_games)), 2)

    def most_goals(self, id):
        goals_list = []

        for game in self.all_game_teams:
            if game['team_id'] == id:
                goals_list.append(game['goals'])

        return int(max(goals_list))

    def fewest_goals_scored(self, id):
        goals_list = []

        for game in self.all_game_teams:
            if game['team_id'] == id:
                goals_list.append(game['goals'])

        return int(min(goals_list))

    def favorite_opponent(self, id):
        opponent_wins_hash = defaultdict(int)
        opponent_total_games_hash = defaultdict(int)
        opponent_win_percentage_hash = defaultdict(float)

        for game1 in self.all_game_teams:
            if game1['team_id'] == id:
                game_id = game1['game_id']

                for game2 in self.all_game_teams:
                    if game2['game_id'] == game_id and game2['team_id'] != id:
                        opponent_total_games_hash[game2['team_id']] += 1
                        if game2['result'] == "LOSS":
                            opponent_wins_hash[game2['team_id']] += 1

        for opponent in opponent_wins_hash:
            opponent_win_percentage_hash[opponent] += float(
                opponent_wins_hash[opponent]) / float(opponent_total_games_hash[opponent])

        max_wins = 0

        for opponent in opponent_win_percentage_hash:
            max_wins = max(max_wins, opponent_win_percentage_hash[opponent])

        favorite_id = ""

        for opponent in opponent_win_percentage_hash:
            if opponent_win_percentage_hash[opponent] == max_wins:
                favorite_id += opponent

        for team in self.all_teams:
            if team['team_id'] == favorite_id:
                return team['teamName']

    def rival(self, id):
        opponent_loss_hash = defaultdict(int)
        opponent_total_games_hash = defaultdict(int)
        opponent_win_percentage_hash = defaultdict(float)

        for game1 in self.all_game_teams:
            if game1['team_id'] == id:
                game_id = game1['game_id']

                for game2 in self.all_game_teams:
                    if game2['game_id'] == game_id and game2['team_id'] != id:
                        opponent_total_games_hash[game2['team_id']] += 1
                        if game2['result'] == "WIN":
                            opponent_loss_hash[game2['team_id']] += 1

        for opponent in opponent_loss_hash:
            opponent_win_percentage_hash[opponent] += float(
                opponent_loss_hash[opponent]) / float(opponent_total_games_hash[opponent])

        max_loss = 0

        for opponent in opponent_win_percentage_hash:
            max_loss = max(max_loss, opponent_win_percentage_hash[opponent])

        rival_id = ""

        for opponent in opponent_win_percentage_hash:
            if opponent_win_percentage_hash[opponent] == max_loss:
                rival_id += opponent

        for team in self.all_teams:
            if team['team_id'] == rival_id:
                return team['teamName']
