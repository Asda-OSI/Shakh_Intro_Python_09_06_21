print('1)-----------------------------------------------')
my_list = ['cat', 'dog', "frog", 'floppa', 'bird', 'chicken']
result = []
# Я посчитал, что "Элементы на чётных местах" из условия - это элементы с чётными индексами
for index, symbol in enumerate(my_list):
    if index % 2:
        result.append(symbol[::-1])
    else:
        result.append(symbol)
print(result)
#####################################################

print('2)-----------------------------------------------')
my_list = ['arn', 'clf', "asda", 'rkl', 'kkc', 'al']
result = []
for index, symbol in enumerate(my_list):
    if symbol[0] == 'a':
        result.append(symbol)

print(result)
#####################################################

print('3)-----------------------------------------------')
my_list = ['rSran', 'clf', "asda", 'rkl', 'kakc', 'al']
result = []
for index, value in enumerate(my_list):
    if 'a' in value:
        result.append(value)

print(result)
#####################################################

print('4)-----------------------------------------------')
my_list = ['0', 0, 12, 34, 'kakc', 9]
result = []
for index, symbol in enumerate(my_list):
    if isinstance(symbol, str):
        result.append(symbol)

print(result)
#####################################################

print('5)-----------------------------------------------')
my_str = 'somelongstringwithoutspaces'
result = []
for index, symbol in enumerate(set(my_str)):
    if my_str.count(symbol) == 1:
        result.append(symbol)
print(result)
#####################################################

print('6)-----------------------------------------------')
my_str_1 = 'somelongstringwithoutspaces'
my_str_2 = 'another string with spaces'
result = list(set(my_str_1).intersection(set(my_str_2)))
print(result)
#####################################################

print('7)-----------------------------------------------')
my_str_1 = 'somelongstringwithoutspaces'
my_str_2 = 'another string with spaces'
result = []
# for index_1, symbol_1 in enumerate(my_str_1):
#     if my_str_1.count(symbol_1) == 1:
#         my_list_1.append(symbol_1)
# for index_2, symbol_2 in enumerate(my_str_2):
#     if my_str_2.count(symbol_2) == 1:
#         my_list_2.append(symbol_2)
my_list = list(set(my_str_1).intersection(set(my_str_2)))
for index, symbol in enumerate(my_list):
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        result.append(symbol)
print(result)
####################################################

print('8)-----------------------------------------------')
dima = {'Фамилия': 'Шарипов',
        'Имя': 'Дмитрий',
        'Возраст': 21,
        'Проживание': {
            'Страна': 'Украина',
            'Город': 'Днепр',
            'Улица': 'пр. Слобожанский'
        },
        'Работа': {
            'Наличие': True,
            'Должность': 'React developer'
        }}
print(dima)
####################################################

print('9)-----------------------------------------------')
# Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
units = 'г'
fake_cake = {'Составляющие': {'Коржи': {'Мука': f'200{units}',
                                        'Молоко': f'400{units}',
                                        'Масло': f'40{units}',
                                        'Яйцо': f'80{units}'
                                        },
                              'Крем': {'Сахар': f'20{units}',
                                       'Масло': f'10{units}',
                                       'Ваниль': f'30{units}',
                                       'Сметана': f'300{units}'
                                       },
                              'Глазурь': {'Какао': f'18{units}',
                                          'Сахар': f'15{units}',
                                          'Масло': f'30{units}'
                                          }
                              }
             }
print(fake_cake)
