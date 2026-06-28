import requests

from config import GEO_URL, WEATHER_URL, OUTPUT_FILE

def get_city(city):
    params = {
        "name": city,
        "count": 1,
        "language": 'en',
        "format": 'json',
    }

    response = requests.get(GEO_URL, params)
    data = response.json()
    return data['results'][0]

def get_weather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
         "current": "temperature_2m,weather_code,wind_speed_10m",
    }

    response = requests.get(WEATHER_URL, params)
    return response.json()

