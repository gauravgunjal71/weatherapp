from django.shortcuts import render, redirect
import requests
import json

# Create your views here.


def home(request):
    with open('./weather/static/city.list.min.json') as f:
        city_list = json.load(f)
    return render(request, 'index.html')


def getweather(request):
    if request.method == 'POST':
        cityname = request.POST.get('city')
        error = ""
        lat=""
        lon=""

        with open('./weather/static/city.list.min.json') as f:
            city_list = json.load(f)

        for i in city_list:
            if(i["name"].lower() == cityname.lower()):
                error = ""
                lat = i["coord"]["lat"]
                lon = i["coord"]["lon"]
                break;
            else:
                error = "Enter Correct City Name"

        if (lat and lon):
            print(lat)
            print(lon)


    return render(request, 'index.html', {'error': error})
