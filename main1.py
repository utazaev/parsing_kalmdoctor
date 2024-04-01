import requests
from bs4 import BeautifulSoup
from ortodont_det import get_ortodont
import json

# get_ortodont()  # функция вызывает парсинг с сайта. закомментирована чтобы не парсить постоянно пока пишу код

with open('ortodont_detsky16032024.json', encoding='utf-8') as f:
    data = json.load(f)


# print(type(data)) #
# print(data['response'][2][2]['date_end']['day']) # печать записи Запись недоступна


dict_len = int(len(data['response'])) # с помощью len определяем количество элементов в подсловаре response в json
# файле и переводим в целое число


for i in range(0, dict_len):                    # прохоимся по всем элементам словаря
    for item01 in data['response'][i]:          # находим ключи словаря и печатем нужные нам значения словаря
        print(item01['date_start']['iso'], item01['date_end']['iso'], item01['denyCause'])

