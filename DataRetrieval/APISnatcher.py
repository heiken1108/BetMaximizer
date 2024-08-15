import requests

NT_baseUrl = "https://api.norsk-tipping.no/OddsenGameInfo/v1/api/"

def get_data_by_url_and_key(url, key):
    try:
        response = requests.get(url)
        return response.json()[key]
    except:
        print("Error: Could not retrieve data from " + url)
        return []

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