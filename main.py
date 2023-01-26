import requests
from pprint import pp
import json

DOMAIN = "https://api.hh.ru/"
"""
regions = requests.get(f"{DOMAIN}/areas/113")
for area in regions.json()['areas']:
    if area['name'] == 'Санкт-Петербуг':
        print(area)
"""
data = {
    'alchemy': 0,
    'asyncio': 0,
    'django': 0,
    'docker': 0,
    'fastapi': 0,
    'flask': 0,
    'git': 0,
    'kubernetes': 0,
    'mongo': 0,
    'mysql': 0,
    'numpy': 0,
    'postgres': 0,
    'rest': 0,
    'sql': 0
}

text_for_file = "Список компаний по запросу:"
text = ""

for i in range(1,21):
    params = {
        "text": "python",
        "page": str(i),
        "area": "2", #Санкт-Петербург
        "professional_role": "96" #Программист-разработчик
    }
    result = requests.get(f"{DOMAIN}vacancies", params=params)

    for item in result.json()['items']:

        if "python" in item['name'].lower():
            text_for_file += f"\n\nДолжность: {item['name']}.\nЗарплата: {str(item['salary']['from']) + '-' + str(item['salary']['to']) if item['salary'] != None else 'Не указана'}.\nТребования: {item['snippet']['requirement']}.\nОбязанности: {item['snippet']['responsibility']}."
            text += item['snippet']['requirement']

for key in data.keys():
    number = text.lower().count(key)
    data[key] = number

with open(r"data\statistics.json", 'w') as file:
    file.write(json.dumps(data))
    
with open("data\\full_info.txt", "w", encoding='utf8') as file:
    file.write(text_for_file)

pp(data)