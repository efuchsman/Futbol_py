from .league_stats import LeagueStats
from .game_stats import GameStats
from .team_stats import TeamStats
from .season_stats import SeasonStats
import pdb


class StatTracker():
    def __init__(self):
        self.league_stats = LeagueStats()
        self.game_stats = GameStats()
        self.team_stats = TeamStats()
        self.season_stats = SeasonStats()

        self.highest_total_score = self.game_stats.highest_total_score()
        self.lowest_total_score = self.game_stats.lowest_total_score()
        self.percentage_home_wins = self.game_stats.percentage_home_wins()
        self.percentage_visitor_wins = self.game_stats.percentage_visitor_wins()
        self.percentage_ties = self.game_stats.percentage_ties()
        self.count_of_games_by_season = self.game_stats.count_of_games_by_season()
        self.average_goals_per_game = self.game_stats.average_goals_per_game()
        self.average_goals_by_season = self.game_stats.average_goals_by_season()

        self.count_of_teams = self.league_stats.count_of_teams()
        self.best_offense = self.league_stats.best_offense()
        self.worst_offense = self.league_stats.worst_offense()
        self.highest_scoring_visitor = self.league_stats.highest_scoring_visitor()
        self.highest_scoring_home_team = self.league_stats.highest_scoring_home_team()
        self.lowest_scoring_visitor = self.league_stats.lowest_scoring_visitor()
        self.lowest_scoring_home_team = self.league_stats.lowest_scoring_home_team()

    def winningest_coach(self, season_id):
        return self.season_stats.winningest_coach(season_id)

    def worst_coach(self, season_id):
        return self.season_stats.worst_coach(season_id)

    def most_accurate_team(self, season_id):
        return self.season_stats.most_accurate_team(season_id)

    def least_accurate_team(self, season_id):
        return self.season_stats.least_accurate_team(season_id)

    def most_tackles(self, season_id):
        return self.season_stats.most_tackles(season_id)

    def fewest_tackles(self, season_id):
        return self.season_stats.least_tackles(season_id)

    def team_info(self, id):
        return self.team_stats.team_info(id)

    def best_season(self, id):
        return self.team_stats.best_season(id)

    def worst_season(self, id):
        return self.team_stats.worst_season(id)

    def average_win_percentage(self, id):
        return self.team_stats.average_win_percentage(id)

    def most_goals_scored(self, id):
        return self.team_stats.most_goals(id)

    def fewest_goals_scored(self, id):
        return self.team_stats.fewest_goals_scored(id)

    def favorite_opponent(self, id):
        return self.team_stats.favorite_opponent(id)

    def rival(self, id):
        return self.team_stats.rival(id)
