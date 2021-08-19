# область видимости в классах
# наследование в классах


##############################################
import os
import string
import random


class WorkWithFiles:
    def __init__(self, dirname='alphabet'):
        self._dirname = dirname
        self.create_dir()

    def _create_dir(self):
        os.makedirs(self._dirname, exist_ok=True)

    def _create_file(self, symbol):
        filename = f'{self._dirname}/{symbol}.txt'
        with open(filename, 'w') as txt_file:
            txt_file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))

    def create_files_in_dir(self):
        for letter in string.ascii_lowercase:
            self._create_file(letter)

    def get_tanos_click(self):
        files = os.listdir(self._dirname)
        files = list(set(files))[:len(files) // 2]
        for file in files:
            os.remove(os.path.join(self._dirname, file))


file_worker = WorkWithFiles('qwe')
file_worker.create_files_in_dir()
file_worker.get_tanos_click()



