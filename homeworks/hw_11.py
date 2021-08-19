import json


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
    for dict in dicts_list:
        splited_name = dict['name'].split(' ')
        dict['name'] = splited_name

    sorted_by_last_name_list = sorted(dicts_list, key=lambda x: (x['name'][-1], x['name'][0]))
    for dict in sorted_by_last_name_list:
        joined_name = ' '.join(dict['name'])
        dict['name'] = joined_name
    return sorted_by_last_name_list


print(f'Sorted by last name: {sort_by_last_name("data.json")}')


# 3. Написать функцию сортировки по дате смерти из поля "years".


def sort_by_year(path):
    dicts_list = read_json(path)
    for dict in dicts_list:
        splited_years = dict['years'].split(' ')
        dict['years'] = splited_years
        if dict['years'][-1] == 'BC.':
            dict['years'][-2] = f'-{dict["years"][-2]}'
            dict['years'].pop(-1)

    sorted_by_year_list = sorted(dicts_list, key=lambda x: float(x['years'][-1]))
    for dict in sorted_by_year_list:
        if float(dict['years'][-1]) < 0:
            dict['years'][-1] = dict['years'][-1].replace('-', '')
            dict['years'].append('BC.')
        joined_year = ' '.join(dict['years'])
        dict['years'] = joined_year
    return sorted_by_year_list


print(f'Sorted by last year: {sort_by_year("data.json")}')


# 4. Написать функцию сортировки по количеству слов в поле "text"


def sort_by_words_number(path):
    dicts_list = read_json(path)
    for dict in dicts_list:
        splited_text = dict['text'].split(' ')
        dict['text'] = splited_text
    sorted_by_words_number_list = sorted(dicts_list, key=lambda x: len(x.get('text')))
    for dict in sorted_by_words_number_list:
        joined_text = ' '.join(dict['text'])
        dict['text'] = joined_text
    return sorted_by_words_number_list


print(f'Sorted by words number in text field: {sort_by_words_number("data.json")}')
