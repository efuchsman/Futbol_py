from .league_stats import LeagueStats
from .game_stats import GameStats
from .team_stats import TeamStats
from .season_stats import SeasonStats


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
        self.highest_scoring_visitor = self.league_stats.highest_scoring_visitor()
        self.highest_scoring_home_team = self.league_stats.highest_scoring_home_team()
        self.lowest_scoring_visitor = self.league_stats.lowest_scoring_visitor()
        self.lowest_scoring_home_team = self.league_stats.lowest_scoring_home_team()
