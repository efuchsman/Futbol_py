from collections import defaultdict
from .league_stats import LeagueStats
from .game_stats import GameStats
import pdb


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
