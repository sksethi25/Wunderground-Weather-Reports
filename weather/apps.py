from __future__ import unicode_literals
from django.apps import AppConfig
import os

class WeatherConfig(AppConfig):
  name = 'weather'
  wukey = os.environ['WU_KEY']
  wcondition = (
  ('tempm','Temperature'),
  ('humidity','Humidity'),
  ('dewptm', 'Dew'),
  ('vism', 'Visibility'),
  ('pressurem', 'Pressure'),
  ('wspdm', 'Wind Speed')
  )