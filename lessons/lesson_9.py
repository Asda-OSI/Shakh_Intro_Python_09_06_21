# Стандартные бибилотеки
# Функции, область видимости, параметры, параметры по умолчанию, типизация

# import string
import random
# import random as rnd

# print(string.punctuation)

value = random.randint(100, 200)
my_list = [1, 2, 3, 10, 20, 30]
# my_list = [True, False]
my_str = 'qwerty'
choice_from_list = random.choice(my_str)
print(value, choice_from_list)
# new_list = random.shuffle(my_list) # стандартная ошибка
new_list = my_list.copy()  # меняет объект!!! поэтому нужно copy
random.shuffle(new_list)
print(my_list, my_list)


# from random import randint, choice
#
# my_str = 'qwerty'
# choice_from_list = choice(my_str)
# value = randint(100, 200)
# print(value, choice_from_list)