import grequests
import requests
from pprint import pp
import json
from time import perf_counter
import logging


DOMAIN = "https://api.hh.ru/"
HH_DOMAIN = "https://api.hh.ru/"
logging.basicConfig(filename="test.log", level=logging.DEBUG, format="%(message)s")


class Parser:
    """
    При создании класса укажите домен, метод и параметры.
    """
    def __init__(self, domain: str, url: str, params: dict, data = None):
        self.domain = domain
        self.url = url
        self.params = params
        self.data = data

    
    def get_num_pages(self):
        result = requests.get(url=f"{self.domain}{self.url}?{'&'.join([key +'='+ val for key, val in self.params.items()])}")
        return int(result.json()['pages'])

    def parse_pages(self):
        page_list = [f"{self.domain}{self.url}?{'&'.join([key+'='+val+'&page='+str(i) for key, val in self.params.items()])}" for i in range(1, self.get_num_pages() + 1)]
        url_list = []
        resp = (grequests.get(page) for page in page_list)
        result = grequests.map(resp)
        for res in result:
            url_list += [vac['url'] for vac in res.json()['items']]
        try:
            resp = (grequests.get(url) for url in url_list)
        except Exception as ex:
            print(ex)
        else:
            result = grequests.map(resp)
            parsed_data = [res.json()['key_skills'] for res in result]
            data = {}
            for lst in parsed_data:
                for dct in lst:
                    if dct['name'].lower() in data.keys():
                        data[dct['name'].lower()] += 1
                    else:
                        data[dct['name'].lower()] = 1
            new_data = {}
            for key in data:
                if data[key] > 4:
                    new_data[key] = data[key]
            self.data = new_data
            return new_data

    def save_data_to_file(self, file_name: str):
        """
        Введите имя файла c расширением .json
        """
        try:
            with open(f"data/{file_name}", 'w', encoding="utf8") as file:
                file.write(json.dumps(self.data))
        except Exception as ex:
            return ex
        else:
            return "Файл успешно добавлен!"


"""
def main():
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
        if data[key] > 4:
            new_data[key] = data[key]
    pp(new_data)
    with open("data/statistics.json", 'w') as file:
            file.write(json.dumps(new_data))

"""
hh = Parser(HH_DOMAIN, url="vacancies", params={
    "text": "python",
    "area": "2", #Санкт-Петербург
    "professional_role": "96" #Программист-разработчик
    })


if __name__ == "__main__":
    start = perf_counter()
    print(hh.parse_pages())
    print(hh.save_data_to_file("new_statistics"))
    print(f"Время выполнения: {(perf_counter() - start):.03f}")
