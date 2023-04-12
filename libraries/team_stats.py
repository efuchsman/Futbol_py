from collections import defaultdict
from .league_stats import LeagueStats
from .game_stats import GameStats


class TeamStats(GameStats, LeagueStats):
    def __init__(self):
        self.game_stats = GameStats()
        self.league_stats = LeagueStats()
        self.all_teams = self.league_stats.all_teams
