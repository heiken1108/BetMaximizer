import os
import pandas as pd
#Class for retrieving hsitoric data about games. Stores 

class DataFetch:
  def __init__(self, start_year, end_year, filename, leagues = [], cols = []):
    self.filename = filename
    self.start_year = start_year
    self.end_year = end_year
    self.seasons = self.generate_seasons()
    self.leagues = leagues
    self.data = pd.DataFrame()
    self.cols = cols

  def prepare_football_data(self):
    print("Preparing football data")
    self.data = self.get_football_data()
    self.store_data_to_csv()

  def get_football_data(self) -> pd.DataFrame:
    url_template = "https://www.football-data.co.uk/mmz4281/{season}/{league}.csv"

    df_ls = []
    for season in self.seasons:
      for league in self.leagues:
        url = url_template.format(season=season, league=league)
        df = self.fetch_data_from_url(url)
        existing_cols = [col for col in self.cols if col in df.columns]
        df = df[existing_cols]
        df_ls.append(df)

    return pd.concat(df_ls)

  def fetch_data_from_url(self, url) -> pd.DataFrame:
    try:
      df = pd.read_csv(url)
      return df
    except:
      print("Error: Could not retrieve data from " + url)
      return pd.DataFrame()

  def generate_seasons(self):
    seasons = []
    for year in range(self.start_year, self.end_year):
      start = str(year)[-2:]
      end = str(year + 1)[-2:]
      seasons.append(start + end)
    return seasons
  

  def store_data_to_csv(self):
    folder_path = os.path.join('.', 'Data', f'{self.filename}_{self.start_year}_{self.end_year}')
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f'Raw_{self.filename}_{self.start_year}_{self.end_year}.csv')
    self.data.to_csv(file_path, index=False)


if __name__ == "__main__":
  filename = "football_data"
  start_year = 2020
  end_year = 2021
  leagues = ['E0']
  cols = [
    "Div",
    "Date",
    "HomeTeam",
    "AwayTeam",
    "FTHG",
    "FTAG",
    "FTR",
    "HTHG",
    "HTAG",
    "HTR",
    "Referee",
    "HS",
    "AS",
    "HST",
    "AST",
    "HF",
    "AF",
    "HC",
    "AC",
    "HY",
    "AY",
    "HR",
    "AR",
    "PSH",
    "PSD",
    "PSA",
    "HBP"
  ]
  DataPrep = DataFetch(start_year, end_year, filename, leagues, cols)
  DataPrep.prepare_football_data()
