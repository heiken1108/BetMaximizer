import DataRetrieval.APISnatcher as APISnatcher
import UtilityFunctions.UtilityFunctions as UtilityFunctions

data = APISnatcher.FootballData_get_tennis_data_by_year_and_tournament('2024', 'ausopen')

print(data)