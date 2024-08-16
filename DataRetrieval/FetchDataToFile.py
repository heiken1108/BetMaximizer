import os
import APISnatcher as APISnatcher

old_seasons = ['E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'I1', 'I2', 'SP1', 'SP2', 'F1', 'F2', 'N1', 'B1', 'P1', 'T1', 'G1']
new_seasons = ['ARG', 'AUT', 'BRA', 'CHN', 'DNK', 'FIN', 'IRL', 'JPN', 'MEX', 'NOR', 'POL', 'ROU', 'RUS', 'SWE', 'SWZ', 'USA']

def generate_seasons(start_year, end_year):
    seasons = []
    for year in range(start_year, end_year):
        start = str(year)[-2:]
        end = str(year + 1)[-2:]
        seasons.append(start + end)
    return seasons

def get_football_data_to_csv_file(file_name):
    data = APISnatcher.get_FootballData(generate_seasons(1980, 2024), old_seasons)
    folder_path = os.path.join('..', 'Files')
    
        
    file_path = os.path.join(folder_path, f'{file_name}.csv')
    data.to_csv(file_path, index=False)

get_football_data_to_csv_file('Football_data_All_Leagues_All_Seasons')