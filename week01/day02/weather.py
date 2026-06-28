from api import get_city, get_weather
from config import OUTPUT_FILE
import json

city = input('请输入城市英文名：')
coordinate  = get_city(city)

data = {}
current = {}

if coordinate:
    name = coordinate.get('name')
    latitude = coordinate.get('latitude')
    longitude = coordinate.get('longitude')

    data = get_weather(latitude, longitude)
    current = data.get('current', {})
    temperature = current.get('temperature_2m')
    print(f"当前城市{name}: {temperature}")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
else:
    print("获取失败")

    

