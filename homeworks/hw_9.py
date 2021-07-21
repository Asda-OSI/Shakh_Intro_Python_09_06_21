print('1)-----------------------------------------------')


def reverse_even_str_generator(some_list: list) -> list:
    # Я посчитал, что "Элементы на чётных местах" из условия - это элементы с чётными индексами
    new_str_list = []
    for index, symbol in enumerate(some_list):
        if index % 2:
            new_str_list.append(symbol[::-1])
        else:
            new_str_list.append(symbol)
    return new_str_list


str_list = ['cat', 'dog', "frog", 'floppa', 'bird', 'chicken']
result = reverse_even_str_generator(str_list)
print(result)
#####################################################

print('2)-----------------------------------------------')


def first_a_checker(some_list: list) -> list:
    new_str_list = []
    for index, symbol in enumerate(some_list):
        if symbol[0] == 'a':
            new_str_list.append(symbol)
    return new_str_list


str_list = ['arn', 'clf', "asda", 'rkl', 'kakc', 'al']
result = first_a_checker(str_list)
print(result)
#####################################################

print('3)-----------------------------------------------')


def a_checker(some_list: list) -> list:
    new_str_list = []
    for index, value in enumerate(some_list):
        if 'a' in value:
            new_str_list.append(value)
    return new_str_list


str_list = ['rSran', 'clf', "asda", 'rkl', 'kakc', 'al']
result = a_checker(str_list)
print(result)
#####################################################

print('4)-----------------------------------------------')


def list_str_checker(some_list: list) -> list:
    new_list = []
    for index, symbol in enumerate(some_list):
        if isinstance(symbol, str):
            new_list.append(symbol)
    return new_list


my_list = ['0', 0, 12, 34, 'kakc', 9]
result = list_str_checker(my_list)
print(result)
#####################################################

print('5)-----------------------------------------------')


def unique_str_symbols_list(some_str: str) -> list:
    new_list = []
    for index, symbol in enumerate(set(some_str)):
        if some_str.count(symbol) == 1:
            new_list.append(symbol)
    return new_list


my_str = 'somelongstringwithoutspaces'
result = unique_str_symbols_list(my_str)
print(result)
#####################################################

print('6)-----------------------------------------------')


def str_intersection(some_str_1: str, some_str_2: str) -> list:
    new_list = list(set(some_str_1).intersection(set(some_str_2)))
    return new_list


my_str_1 = 'somelongstringwithoutspaces'
my_str_2 = 'another string with spaces'
result = str_intersection(my_str_1, my_str_2)
print(result)
#####################################################

print('7)-----------------------------------------------')


def unique_two_str_symbols_list(some_str_1: str, some_str_2: str) -> list:
    new_list = []
    some_list = list(set(some_str_1).intersection(set(some_str_2)))
    for index, symbol in enumerate(some_list):
        if some_str_1.count(symbol) == 1 and some_str_2.count(symbol) == 1:
            new_list.append(symbol)
    return new_list


my_str_1 = 'somelongstringwithoutspaces'
my_str_2 = 'another string with spaces'
result = unique_two_str_symbols_list(my_str_1, my_str_2)
print(result)
####################################################

print('8)-----------------------------------------------')
import random
import string

names = ['Smith', 'Jonson', 'Williams', 'Garcia', 'Davis', 'Garcia', 'Jones', 'Green', 'Adams']
domains = ['com', 'net', 'org', 'in', 'uk', 'co', 'us', 'ua', 'uk', 'au', 'de']


def email_generator(names_list: list, domains_list: list) -> str:
    random_name = random.choice(names_list).lower()
    random_number = random.randint(100, 999)
    letters = string.ascii_lowercase
    random_letters_list = []
    for count in range(random.randint(5, 7)):
        random_letter = random.choice(letters);
        random_letters_list.append(random_letter)
    random_letter_str = ''.join(random_letters_list)
    random_domain = random.choice(domains_list)
    email = f'{random_name}.{random_number}@{random_letter_str}.{random_domain}'
    return email


random_email = email_generator(names, domains)
print(random_email)
