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
