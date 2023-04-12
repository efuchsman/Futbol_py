from collections import defaultdict
from .league_stats import LeagueStats
from .game_stats import GameStats


class SeasonStats(GameStats, LeagueStats):
    def __init__(self):
        self.game_stats = GameStats()
        self.league_stats = LeagueStats()

    def season_games(self, season_id):
        season_id_games = [game['game_id']
                           for game in self.game_stats.all_games if game['season'] == season_id]
        return season_id_games

    def season_shots(self, season_id):
        team_season_shots_hash = defaultdict(int)
        team_season_goals_hash = defaultdict(int)
        team_season_accuracy_hash = defaultdict(float)

        for id in self.season_games(season_id):

            for game_team in self.league_stats.all_game_teams:
                if game_team['game_id'] == id:
                    team_season_goals_hash[game_team['team_id']
                                           ] += int(game_team['goals'])
                    team_season_shots_hash[game_team['team_id']
                                           ] += int(game_team['shots'])

        for team in team_season_goals_hash:
            team_season_accuracy_hash[team] += float(
                team_season_goals_hash[team]) / float(team_season_shots_hash[team])

        return team_season_accuracy_hash

    def season_tackles(self, season_id):
        team_season_tackle_hash = defaultdict(int)

        for id in self.season_games(season_id):
            for game_team in self.league_stats.all_game_teams:
                if game_team['game_id'] == id:
                    team_season_tackle_hash[game_team['team_id']
                                            ] += int(game_team['tackles'])
        return team_season_tackle_hash

    def winningest_coach(self, season_id):
        coach_season_wins_hash = defaultdict(int)
        coach_season_total_games_hash = defaultdict(int)
        coach_season_percentage_hash = defaultdict(float)

        for id in self.season_games(season_id):

            for game_team in self.league_stats.all_game_teams:
                if game_team['game_id'] == id:
                    coach_season_total_games_hash[game_team['head_coach']
                                                  ] += 1
                    if game_team['result'] == "WIN":
                        coach_season_wins_hash[game_team['head_coach']] += 1

        for coach in coach_season_wins_hash:
            coach_season_percentage_hash[coach] += float(
                coach_season_wins_hash[coach]) / float(coach_season_total_games_hash[coach])

        max_ratio = 0

        for coach in coach_season_percentage_hash:
            max_ratio = max(
                max_ratio, coach_season_percentage_hash[coach])

        for coach in coach_season_percentage_hash:
            if coach_season_percentage_hash[coach] == max_ratio:
                return coach

    def worst_coach(self, season_id):
        coach_season_loss_hash = defaultdict(int)
        coach_season_total_games_hash = defaultdict(int)
        coach_season_percentage_hash = defaultdict(float)

        for id in self.season_games(season_id):

            for game_team in self.league_stats.all_game_teams:
                if game_team['game_id'] == id and game_team['result'] != "TIE":
                    coach_season_total_games_hash[game_team['head_coach']
                                                  ] += 1
                    if game_team['result'] == "LOSS":
                        coach_season_loss_hash[game_team['head_coach']] += 1

        for coach in coach_season_loss_hash:
            coach_season_percentage_hash[coach] += float(
                coach_season_loss_hash[coach]) / float(coach_season_total_games_hash[coach])

        worst_ratio = 0

        for coach in coach_season_percentage_hash:
            worst_ratio = max(worst_ratio,
                              coach_season_percentage_hash[coach])

        for coach in coach_season_percentage_hash:
            if coach_season_percentage_hash[coach] == worst_ratio:
                return coach

    def most_accurate_team(self, season_id):

        team_season_accuracy_hash = self.season_shots(season_id)
        best_accuracy = 0

        for team in team_season_accuracy_hash:
            best_accuracy = max(best_accuracy, team_season_accuracy_hash[team])

        top_accurate_team = ""

        for team in team_season_accuracy_hash:
            if team_season_accuracy_hash[team] == best_accuracy:
                top_accurate_team += team

        for team in self.league_stats.all_teams:
            if team['team_id'] == top_accurate_team:
                return team['teamName']

    def least_accurate_team(self, season_id):
        team_season_accuracy_hash = self.season_shots(season_id)

        least_accuracy = 1

        for team in team_season_accuracy_hash:
            least_accuracy = min(
                least_accuracy, team_season_accuracy_hash[team])

        bottom_accurate_team = ""

        for team in team_season_accuracy_hash:
            if team_season_accuracy_hash[team] == least_accuracy:
                bottom_accurate_team += team

        for team in self.league_stats.all_teams:
            if team['team_id'] == bottom_accurate_team:
                return team['teamName']

    def most_tackles(self, season_id):
        team_season_tackle_hash = self.season_tackles(season_id)
        max_tackles = 0

        for team in team_season_tackle_hash:
            max_tackles = max(max_tackles, team_season_tackle_hash[team])

        top_accurate_team = ""

        for team in team_season_tackle_hash:
            if team_season_tackle_hash[team] == max_tackles:
                top_accurate_team += team

        for team in self.league_stats.all_teams:
            if team['team_id'] == top_accurate_team:
                return team['teamName']

    def least_tackles(self, season_id):
        team_season_tackle_hash = self.season_tackles(season_id)
        min_tackles = 10000

        for team in team_season_tackle_hash:
            min_tackles = min(min_tackles, team_season_tackle_hash[team])

        top_accurate_team = ""

        for team in team_season_tackle_hash:
            if team_season_tackle_hash[team] == min_tackles:
                top_accurate_team += team

        for team in self.league_stats.all_teams:
            if team['team_id'] == top_accurate_team:
                return team['teamName']
