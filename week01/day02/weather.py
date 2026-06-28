from api import get_city, get_weather
from config import OUTPUT_FILE
import json

city = input('请输入城市英文名：')
coordinate  = get_city(city)

data = get_weather(coordinate['latitude'], coordinate['longitude'])
current = data['current']

print(f"当前城市{coordinate['name']}: {current['temperature_2m']}")

with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)