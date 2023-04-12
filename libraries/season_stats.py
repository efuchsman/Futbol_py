from collections import defaultdict
from .league_stats import LeagueStats
from .game_stats import GameStats
import pdb


class SeasonStats(LeagueStats, GameStats):

    def winningest_coach(self, season_id):
        coach_season_wins_hash = defaultdict(int)
        coach_season_total_games_hash = defaultdict(int)
        coach_season_percentage_hash = defaultdict(int)

        game_stats = GameStats()
        league_stats = LeagueStats()

        season_id_games = []

        for game in game_stats.all_games:
            if game['season'] == season_id:
                season_id_games.append(game['game_id'])

        for id in season_id_games:

            for game_team in league_stats.all_game_teams:
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
            max_ratio = max(max_ratio, coach_season_percentage_hash[coach])

        for coach in coach_season_percentage_hash:
            if coach_season_percentage_hash[coach] == max_ratio:
                return coach

    def worst_coach(self, season_id):
        coach_season_loss_hash = defaultdict(int)
        coach_season_total_games_hash = defaultdict(int)
        coach_season_percentage_hash = defaultdict(int)

        game_stats = GameStats()
        league_stats = LeagueStats()

        season_id_games = []

        for game in game_stats.all_games:
            if game['season'] == season_id:
                season_id_games.append(game['game_id'])

        for id in season_id_games:

            for game_team in league_stats.all_game_teams:
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
            worst_ratio = max(worst_ratio, coach_season_percentage_hash[coach])

        for coach in coach_season_percentage_hash:
            if coach_season_percentage_hash[coach] == worst_ratio:
                return coach

    def most_accurate_team(self, season_id):
        game_stats = GameStats()
        league_stats = LeagueStats()

        team_season_shots_hash = defaultdict(int)
        team_season_goals_hash = defaultdict(int)
        team_season_accuracy_hash = defaultdict(int)

        season_id_games = []

        for game in game_stats.all_games:
            if game['season'] == season_id:
                season_id_games.append(game['game_id'])

        for id in season_id_games:

            for game_team in league_stats.all_game_teams:
                if game_team['game_id'] == id:
                    team_season_goals_hash[game_team['team_id']
                                           ] += int(game_team['goals'])
                    team_season_shots_hash[game_team['team_id']
                                           ] += int(game_team['shots'])

        for team in team_season_goals_hash:
            team_season_accuracy_hash[team] += float(
                team_season_goals_hash[team]) / float(team_season_shots_hash[team])

        best_accuracy = 0

        for team in team_season_accuracy_hash:
            best_accuracy = max(best_accuracy, team_season_accuracy_hash[team])

        top_accurate_team = ""

        for team in team_season_accuracy_hash:
            if team_season_accuracy_hash[team] == best_accuracy:
                top_accurate_team += team

        for team in league_stats.all_teams:
            if team['team_id'] == top_accurate_team:
                return team['teamName']

    def least_accurate_team(self, season_id):
        game_stats = GameStats()
        league_stats = LeagueStats()

        team_season_shots_hash = defaultdict(int)
        team_season_goals_hash = defaultdict(int)
        team_season_accuracy_hash = defaultdict(int)

        season_id_games = []

        for game in game_stats.all_games:
            if game['season'] == season_id:
                season_id_games.append(game['game_id'])

        for id in season_id_games:

            for game_team in league_stats.all_game_teams:
                if game_team['game_id'] == id:
                    team_season_goals_hash[game_team['team_id']
                                           ] += int(game_team['goals'])
                    team_season_shots_hash[game_team['team_id']
                                           ] += int(game_team['shots'])

        for team in team_season_goals_hash:
            team_season_accuracy_hash[team] += float(
                team_season_goals_hash[team]) / float(team_season_shots_hash[team])

        least_accuracy = 1

        for team in team_season_accuracy_hash:
            least_accuracy = min(
                least_accuracy, team_season_accuracy_hash[team])

        bottom_accurate_team = ""

        for team in team_season_accuracy_hash:
            if team_season_accuracy_hash[team] == least_accuracy:
                bottom_accurate_team += team

        for team in league_stats.all_teams:
            if team['team_id'] == bottom_accurate_team:
                return team['teamName']
