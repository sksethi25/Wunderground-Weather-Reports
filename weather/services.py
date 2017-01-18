import json
import requests
from datetime import datetime, timedelta
from .models import Weather, Cities_available, Cities
from django.apps import apps

def parseData(response, date):
  req_keys = {'mintempm': -9999, 'mindewptm': -9999, 'minhumidity': -9999, 
    'minwspdm': -9999, 'minvism': -9999, 'minpressurem': -9999,
    'maxtempm': -9999, 'maxdewptm': -9999, 'maxhumidity': -9999, 
    'maxwspdm': -9999, 'maxvism': -9999, 'maxpressurem': -9999, 
    'weather_date': date
  }

  if response and 'history' in response \
    and 'dailysummary' in response['history'] \
    and len(response['history']['dailysummary'])> 0: 
    daily_data = response['history']['dailysummary'][0]
    for key in req_keys:
      if key in daily_data:
        if daily_data[key] != "":
          req_keys[key]= daily_data[key]
  return req_keys

def request_history(city, date):
  payload = {'key': apps.get_app_config('weather').wukey,'city': city, 'date':format_date(date)}
  urls = "http://api.wunderground.com/api/{key}/history_{date}/q/{city}.json"
  url = urls.format(**payload)
  try:
    res = requests.get(url)
    return parseData(res.json(), date)
  except Exception as e: 
    print(str(e))
    return None

def get_city(city):
  return Cities_available.objects.filter(id=city)[:1]

def format_date(date):
  frmt = '%Y%m%d'
  return date.strftime(frmt)

def get(city, condition, from_date, to_date):
  from_date, to_date = get_date_object(from_date, to_date)
  days = (to_date-from_date).days + 1
  fetch_date = from_date.date()

  req_data = []
  db_fetched_dates = []
  try:
    city_obj = get_city(city)[0]
    weather_data = Weather.objects \
      .filter(weather_date__gte=from_date.date(), weather_date__lte=to_date.date(),city=city_obj) \
      .values("max" + condition, "min"+ condition, 'weather_date') \
      .order_by('weather_date')

    for weather in weather_data:
      db_fetched_dates.append(weather['weather_date'])
      req_data.append(weather)
  except Exception as e: 
    print(str(e))
    return None

  while(days):
    days-=1
    if fetch_date not in db_fetched_dates:
      data_fetched = request_history(city_obj.lat_long, fetch_date)
      if data_fetched:
        data_fetched['city'] = city_obj
        weather_obj = Weather(**data_fetched)
        weather_obj.save()
        required_values= weather_obj.get_values({"max" + condition,  \
          "min"+ condition, 'weather_date'})
        req_data.append(required_values)
    fetch_date = get_next_date(fetch_date)

  return json.dumps(req_data, default=date_handler)

def add_service(cities):
  already_added = list(Cities.objects.values_list('city_id', flat=True))
  for city in cities:
    if int(city) not in already_added:
      cities_obj = Cities(city=get_city(city)[0])
      cities_obj.save()


def date_handler(obj):
    if hasattr(obj, 'strftime'):
        return obj.strftime("%d/%m/%Y")
    else:
        raise TypeError

def get_date_object(from_date, to_date):
  from_date = datetime.strptime(from_date, "%d/%m/%Y")
  to_date = datetime.strptime(to_date, "%d/%m/%Y")
  return from_date, to_date

def get_next_date(date):
  return date + timedelta(days=1)

