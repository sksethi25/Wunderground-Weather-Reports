import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import fetchForm, addCity
from .services import get, add_service
from .models import Cities, Cities_available

def index(request):
  return render(request, 'weather/index.html', {'form': fetchForm()})

def add(request):
  return render(request, 'weather/add.html', {'form': addCity()})

def get_cities(request):
  if request.method == 'GET':
    return HttpResponse(json.dumps(list(Cities_available.objects.values_list('city')
    .filter(id__in=Cities.objects.values_list('city_id')))))

def fetch(request):
  if request.method == 'POST':
    form = fetchForm(request.POST)
    wdata = {}
    if form.is_valid():
      print("returning none1")
      city = form.cleaned_data['select_city']
      condition = form.cleaned_data['select_cond']
      from_date = form.cleaned_data['from_date']
      to_date = form.cleaned_data['to_date']
      wdata = get(city, condition, from_date, to_date)
      print("returning none2")
    return HttpResponse(wdata)

def add_city(request):
  if request.method == 'POST':
    print(request.POST.getlist(add_city))
    form = addCity(request.POST)
    wdata = {}
    if form.is_valid():
      print("returning none1")
      city = form.cleaned_data['add_city']
      print (city)
      add_service(city)
    return HttpResponse("hle")
