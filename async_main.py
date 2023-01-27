import grequests
import requests
from pprint import pp
import json
from time import perf_counter
import logging


DOMAIN = "https://api.hh.ru/"
logging.basicConfig(filename="test.log", level=logging.DEBUG, format="%(message)s")

start = perf_counter()

page_list = [f"{DOMAIN}vacancies?text=c++&page={i}&area=2&professional_role=96" for i in range(1,10)]
url_list = []
data ={}

resp = (grequests.get(page) for page in page_list)
result = grequests.map(resp)
for res in result:
    url_list += [vac['url'] for vac in res.json()['items']]


resp = (grequests.get(url) for url in url_list)
result = grequests.map(resp)
print(result[0].json()['errors'][0]['captcha_url'])
parsed_data = [res.json()['key_skills'] for res in result]

for lst in parsed_data:
    for dct in lst:
        if dct['name'].lower() in data.keys():
            data[dct['name'].lower()] += 1
        else:
            data[dct['name'].lower()] = 1
new_data = {}
for key in data:
    if data[key] > 5:
        new_data[key] = data[key]
pp(new_data)
"""
for page in page_list:
    result = requests.get(url=page)
    url_list += [vac['url'] for vac in result.json()['items']]

skill_list = [requests.get(url=url).json()['key_skills'] for url in url_list]
print(skill_list)
"""
print(f"Время выполнения: {(perf_counter() - start):.03f}")
