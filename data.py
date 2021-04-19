from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot

lebronStats = get_stats('LeBron James', stat_type='advanced',playoffs = False,career=False)
kdStats = get_stats('Kevin Durant', stat_type='advanced', playoffs=False, career=False)

print(lebronStats,kdStats)
