from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc

lakers = get_team_stats("LAL",2019)
print(lakers)