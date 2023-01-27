import requests
from pprint import pp
import json
from time import perf_counter

DOMAIN = "https://api.hh.ru/"
"""
regions = requests.get(f"{DOMAIN}/areas/113")
for area in regions.json()['areas']:
    if area['name'] == 'Санкт-Петербуг':
        print(area)
"""

def main():
    data = {}

    text_for_file = "Список компаний по запросу:"
    text = ""
    for i in range(1,25):
        params = {
            "text": "python",
            "page": str(i),
            "area": "2", #Санкт-Петербург
            "professional_role": "96" #Программист-разработчик
        }
        result = requests.get(f"{DOMAIN}vacancies", params=params)
        #pp(requests.get(result.json()['items'][0]['url']).json()['key_skills'])

        for item in result.json()['items']:
            for skill in requests.get(item['url']).json()['key_skills']:
                if skill['name'].lower() in data:
                    data[skill['name'].lower()] += 1
                else:
                    data[skill['name'].lower()] = 1
    new_data = {}
    for key in data:
        if data[key] > 5:
            new_data[key] = data[key]
    print(new_data)

    """
            if "python" in item['name'].lower():
                text_for_file += f"\n\nДолжность: {item['name']}.\nЗарплата: {str(item['salary']['from']) + '-' + str(item['salary']['to']) if item['salary'] != None else 'Не указана'}.\nТребования: {item['snippet']['requirement']}.\nОбязанности: {item['snippet']['responsibility']}."
                text += item['snippet']['requirement']

    for key in data.keys():
        number = text.lower().count(key)
        data[key] = number
    
    with open("data/statistics.json", 'w') as file:
        file.write(json.dumps(data))
        
    with open("data/full_info.txt", "w", encoding='utf8') as file:
        file.write(text_for_file)
    
    pp(data)
    """
if __name__ == "__main__":
    start = perf_counter()
    main()
    print(f"Время: {(perf_counter() - start):.03f}")