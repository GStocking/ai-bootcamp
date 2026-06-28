import requests

from config import GEO_URL, WEATHER_URL

def get_city(city):
    params = {
        "name": city,
        "count": 1,
        "language": 'en',
        "format": 'json',
    }
    try:
        response = requests.get(GEO_URL, params=params)
        data = response.json()
        results = data.get("results")
        print("city response:", data)
        if not results:
            return None
        return results[0]
    except Exception as e:
        print('解析失败', e)

def get_weather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
         "current": "temperature_2m,weather_code,wind_speed_10m",
    }

    try:
        response = requests.get(WEATHER_URL, params=params)
        print("weather text:", response.text)

        result = response.json()
        print("weather json:", result)
        return result
    except Exception as e:
        print('解析失败', e)

