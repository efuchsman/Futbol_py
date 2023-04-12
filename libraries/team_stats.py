from collections import defaultdict
from .league_stats import LeagueStats
from .game_stats import GameStats


class TeamStats(GameStats, LeagueStats):
    def __init__(self):
        self.game_stats = GameStats()
        self.league_stats = LeagueStats()
        self.all_teams = self.league_stats.all_teams

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
