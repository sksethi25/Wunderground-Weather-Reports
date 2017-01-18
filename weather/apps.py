from __future__ import unicode_literals
from django.apps import AppConfig

class WeatherConfig(AppConfig):
  name = 'weather'
  wukey = "ADD Wu key here"
  wcondition = (
  ('tempm','Temperature'),
  ('humidity','Humidity'),
  ('dewptm', 'Dew'),
  ('vism', 'Visibility'),
  ('pressurem', 'Pressure'),
  ('wspdm', 'Wind Speed')
  )