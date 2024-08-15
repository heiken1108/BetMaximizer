#Format: Year: 24, num_seasons: 3
def get_season_strings_list(start_year, num_seasons):
  season_strings = []
  for i in range(start_year, start_year + num_seasons):
    season_strings.append(f"{i}{i+1}")
  return season_strings

def get_all_old_Divisions():
  return ['E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'I1', 'I2', 'SP1', 'SP2', 'F1', 'F2', 'N1', 'B1', 'P1', 'T1', 'G1']

def get_all_new_Divisions():
  return ['ARG', 'AUT', 'BRA', 'CHN', 'DNK', 'FIN', 'IRL', 'JPN', 'MEX', 'NOR', 'POL', 'ROU', 'RUS', 'SWE', 'SWZ', 'USA']