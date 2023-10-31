import requests
from django.shortcuts import render


def index(request):
    apiId = '6949a2808723bdd6406ed4175fdea64d'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + apiId

    city = 'London'
    responce = requests.get(url.format(city)).json()

    city_info = {
        'city' : city,
        'temp' : responce["main"]["temp"],
        'icon' : responce["weather"][0]["icon"]
    }

    context = { 'info' : city_info }

    return render(request, 'weather/index.html', context)