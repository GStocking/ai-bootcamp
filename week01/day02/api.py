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
        response = requests.get(GEO_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        results = data.get("results")

        if not results:
            return None
        
        return results[0]
    except requests.RequestException as e:
        print('请求接口解析失败', e)
        return None
    except ValueError as e:
        print('解析接口解析失败', e)
        return None


def get_weather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
         "current": "temperature_2m,weather_code,wind_speed_10m",
    }

    try:
        response = requests.get(WEATHER_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    
    except requests.RequestException as error:
        print(f"请求天气接口失败: {error}")
        return None
    except ValueError as error:
        print(f"解析天气接口 JSON 失败: {error}")
        return None

