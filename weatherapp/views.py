import datetime

import requests
from django.shortcuts import render


def index(request):
    city = request.GET.get('city')
    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid=2073fb3f4d68dbbd005c6134ec9a14a6")
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today()
    context = {
        'day': day,
        'city': city,
        'description': description,
        'icon': icon,
        'temp': temp
    }
    return render(request, 'index.html', context=context)
