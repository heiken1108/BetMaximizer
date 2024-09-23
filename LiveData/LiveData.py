import requests

class LiveData:
  def __init__(self):
    self.base_url = 'https://api.norsk-tipping.no/OddsenGameInfo/v1/api/'

  def NT_get_all_events_by_sport_id(self, sportId):
    return fetch_from_url(self.base_url + "events/" + sportId, 'eventList')

  def NT_get_all_events_by_sport_id_and_date(self, sportId, date):
    return fetch_from_url(self.base_url + "events/" + sportId + "/" + date, 'eventList')
  
  def NT_get_all_events_by_sport_id_and_date_interval(self, sportId, startDate, endDate):
    return fetch_from_url(self.base_url + "events/" + sportId + "/" + startDate + "/" + endDate, 'eventList')
  
  def NT_get_live_events_by_sport_id(self, sportId):
    return fetch_from_url(self.base_url + "liveevents/" + sportId, 'eventList')
  
  def NT_get_all_live_events(self):
    return fetch_from_url(self.base_url + "liveevents", 'eventList')
  
  def NT_get_markets_by_event_id(self, eventId):
    return fetch_from_url(self.base_url + "markets/" + eventId, 'markets')
  
  def NT_get_all_sports_names(self):
    return fetch_from_url(self.base_url + "sportTypes", 'sportTypeList')
  
  def NT_get_sport_by_id(self, sportId):
    sports = self.NT_get_all_sports_names()
    for sport in sports:
        if sport['sportId'] == sportId:
            return sport
    return None
  
  def NT_get_all_sports_info(self):
    return fetch_from_url(self.base_url + "sports", 'sports')

def fetch_from_url(url, key = '') -> dict:
  try:
    response = requests.get(url)
    if key == '':
        return response.json()
    else:
        return response.json()[key]
  except:
      print("Error: Could not retrieve data from " + url)
      return []