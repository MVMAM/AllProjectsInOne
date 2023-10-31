import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    apiId = '6949a2808723bdd6406ed4175fdea64d'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + apiId

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        responce = requests.get(url.format(city.name)).json()
        city_info = {
            'city' : city.name,
            'temp' : responce["main"]["temp"],
            'icon' : responce["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {
        'all_info' : all_cities,
        'form' : form
    }

    return render(request, 'weather/index.html', context)