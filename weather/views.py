from django.shortcuts import render, redirect
import requests
import json, urllib.request
import time

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
        api_key = "5ec52009cd2282b3760abc221e82c0d9"
        weather_data = {}

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
            url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(lat) + "&lon=" + str(lon) + "&units=metric&exclude=hourly,minutely,current&appid="+api_key
            response = urllib.request.urlopen(url)
            weather_data = json.loads(response.read())
            weather_data['cityname'] = cityname
            for data in weather_data['daily']:
                date_unix = data['dt']
                date_formatted = time.ctime(date_unix)
                date = date_formatted.split(" ")[0] + " "+  date_formatted.split(" ")[1] + "-"+ date_formatted.split(" ")[2] + "-"+ date_formatted.split(" ")[4]
                data['dt'] = date

            print(weather_data)    


    return render(request, 'index.html', {'error': error, 'weather_data':weather_data})
