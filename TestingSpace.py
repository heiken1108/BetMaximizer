import DataRetrieval.APISnatcher as APISnatcher
import UtilityFunctions.UtilityFunctions as UtilityFunctions

data = APISnatcher.FootballData_get_football_data_by_season_and_league_new('USA')

print(data)