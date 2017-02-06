#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Консольный клиент для open-file.ru
# Версия 1.0
# Дата релиза 2017-02-06


import re
import texttable as tt
from bs4 import BeautifulSoup
import requests
import sys

open_file_url = "http://open-file.ru/search/"


def get_html(search):
    data = requests.post(open_file_url, data={"word": search.replace(' ', '')})
    return data.text if data.text != '' else 'error'


def parse(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    data = {}
    for tab in soup.find_all('table'):
        for row in tab.find_all('tr'):
            tmp = row.find_all('td')
            if len(tmp) == 2:
                data[re.sub(r'\s{3,}', '', tmp[0].text.strip())] = re.sub(r'\s{3,}', '', tmp[1].text.strip())

    result = []
    for tab in soup.find_all('table', attrs={'class': ['tbl']}):
        cols = [col.text for col in tab.find_all('th')]
        for row in tab.find_all('tr'):
            tmp = row.find_all('td')
            if len(tmp) == len(cols):
                result.append({cols[0]: tmp[0].text.strip(), cols[1]: tmp[1].text.strip(), cols[2]: tmp[2].text.strip()})
    return result


def table_viewer(data):
    tab = tt.Texttable()
    header = ['Формат', 'Тип', 'Описание']
    tab.header(header)
    for server in data:
        tab.add_row(server)
    tab.set_cols_width([10, 55, 50])
    tab.set_deco(tab.HEADER | tab.VLINES)
    tab.set_chars(['-', '|', '+', '='])
    return tab.draw()


def main():
    if len(sys.argv) > 1:
        data = []
        for d in parse(get_html(sys.argv[1])):
            line = []
            for key in d:
                line.append(d[key])
            data.append(line)
        return table_viewer(data) if len(data) > 0 else "Ошибка: Раширение не найдено"
    return "Ошибка: Не указан формат.\nПример использования:\n\t file-format jpg"


if __name__ == '__main__':
    print main()
