from django import forms
from django.apps import apps
from .models import Cities_available, Cities

def get_available_cites():
 	return list(Cities_available.objects.values_list('id', 'city'))

def get_cites():
  return list(Cities_available.objects.values_list('id', 'city')
    .filter(id__in=Cities.objects.values_list('city_id')))

class addCity(forms.Form):
  add_city = forms.MultipleChoiceField(choices=get_available_cites, widget=forms.SelectMultiple())

class fetchForm(forms.Form):
  select_city = forms.ChoiceField(label='City', widget=forms.Select
    ,choices=get_cites)
  select_cond = forms.ChoiceField(label='Condition', widget=forms.Select,
    choices=apps.get_app_config('weather').wcondition)
  from_date = forms.CharField(label='From', max_length=10)
  to_date = forms.CharField(label='To', max_length=10)

