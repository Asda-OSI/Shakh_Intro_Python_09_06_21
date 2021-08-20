import json
import re
import string


# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.


def read_json(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        return data


print(f'Json data: {read_json("data.json")}')


# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Если фамилии нет, то использовать имя, например Euclid.


def sort_by_last_name(path):
    dicts_list = read_json(path)
    template = r'[a-zA-Z]+'
    sorted_by_last_name_list = sorted(dicts_list, key=lambda x: (
        re.findall(template, x.get('name'))[-1], re.findall(template, x.get('name'))[0]))
    return sorted_by_last_name_list


print(f'Sorted by last name: {sort_by_last_name("data.json")}')


# 3. Написать функцию сортировки по дате смерти из поля "years".


def sort_by_year(dicts):
    years = dicts.get('years')
    last_year_str = re.findall(r'\d+', years)[-1]
    last_year_int = int(last_year_str)

    death_date = last_year_int if 'BC' not in years else last_year_int * -1

    return death_date


sorted_by_year_list = sorted(read_json('data.json'), key=sort_by_year)
print(f'Sorted by last year: {sorted_by_year_list}')


# 4. Написать функцию сортировки по количеству слов в поле "text"


def sort_by_words_number(path):
    dicts_list = read_json(path)
    template = r"[a-zA-Z0-9'’-]+"
    sorted_by_words_number_list = sorted(dicts_list, key=lambda x: len(re.findall(template, x.get('text'))))
    return sorted_by_words_number_list


print(f'Sorted by words number in text field: {sort_by_words_number("data.json")}')
