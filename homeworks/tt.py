import json


# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.


def read_json(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        return data


print(f'Json data: {read_json("data.json")}')


# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Если фамилии нет, то использовать имя, например Euclid.


def split_name(path):
    dicts_list = read_json(path)
    for dict in dicts_list:
        splited_name = dict['name'].split(' ')
        dict['name'] = splited_name
    return dicts_list


def sort_by_last_name(last_name_dict):
    last_name = last_name_dict['name']
    last_name = last_name[-1]
    first_name = last_name_dict['name']
    first_name = first_name[0]
    return last_name, first_name


def join_name(path):
    sorted_by_last_name_list = sorted(split_name(path), key=sort_by_last_name)
    for dict in sorted_by_last_name_list:
        joined_name = ' '.join(dict['name'])
        dict['name'] = joined_name
    return sorted_by_last_name_list


print(f'Sorted by last name: {join_name("data.json")}')
