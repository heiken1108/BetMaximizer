import requests
import pandas as pd

NT_baseUrl = "https://api.norsk-tipping.no/OddsenGameInfo/v1/api/"

def get_data_by_url_and_key(url, key = ''):
    try:
        response = requests.get(url)
        if key == '':
            return response.json()
        else:
            return response.json()[key]
    except:
        print("Error: Could not retrieve data from " + url)
        return []

#Format: sportId = FBL (Fotball)
def NT_get_all_events_by_sport_id(sportId):
    return get_data_by_url_and_key(NT_baseUrl + "events/" + sportId, 'eventList')


def NT_get_all_events_by_sport_id_and_date(sportId, date):
    return get_data_by_url_and_key(NT_baseUrl + "events/" + sportId + "/" + date, 'eventList')

def NT_get_all_events_by_sport_id_and_date_interval(sportId, startDate, endDate):
    return get_data_by_url_and_key(NT_baseUrl + "events/" + sportId + "/" + startDate + "/" + endDate, 'eventList')

def NT_get_live_events_by_sport_id(sportId):
    return get_data_by_url_and_key(NT_baseUrl + "liveevents/" + sportId, 'eventList')

def NT_get_all_live_events():
    return get_data_by_url_and_key(NT_baseUrl + "liveevents", 'eventList')

def NT_get_markets_by_event_id(eventId):
    return get_data_by_url_and_key(NT_baseUrl + "markets/" + eventId, 'markets')

def NT_get_all_sports_names():
    return get_data_by_url_and_key(NT_baseUrl + "sportTypes", 'sportTypeList')

def NT_get_sport_by_id(sportId):
    sports = NT_get_all_sports_names()
    for sport in sports:
        if sport['sportId'] == sportId:
            return sport
    return None

def NT_get_all_sports_info():
    return get_data_by_url_and_key(NT_baseUrl + "sports", 'sports')

#Format: Season: 2122 (som betyr 2021/2022), League: E0 (Premier League)
def FootballData_get_football_data_by_season_and_league(season, league):
    url = f"https://www.football-data.co.uk/mmz4281/{season}/{league}.csv"
    return pd.read_csv(url)

#Format: Year: 2024, Tournament: ausopen
def FootballData_get_tennis_data_by_year_and_tournament(year, tournament):
    url = f"http://www.tennis-data.co.uk/{year}/{tournament}.csv"
    print(url)
    return pd.read_csv(url)