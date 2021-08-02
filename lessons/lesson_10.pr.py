import os
import string
import random


def create_dir(path):
    os.makedirs(path, exist_ok=True)
    create_files_in_dir(path)


def create_file(path, symbol):
    filename = f'{path}/{symbol}.txt'
    with open(filename, 'w') as txt_file:
        txt_file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))


def create_files_in_dir(path):
    for letter in string.ascii_lowercase:
        create_file(path, letter)


def get_tanos_click(path):
    files = os.listdir(path)
    files = list(set(files))[:len(files) // 2]
    for file in files:
        os.remove(os.path.join(path, file))
    print(files)


create_dir('alphabet')
get_tanos_click('alphabet')


