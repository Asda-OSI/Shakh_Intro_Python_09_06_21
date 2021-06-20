# a = 10
# print(a)
#
# a = 'qwerty'
# print(a)
#
# a = 12 / 4
# print(a)
#
# # PEP-8
# my_value = 12
# string = 'asd'
# pi_ratio = 22 / 7 #snake case
# # pi-ratio = 'Kebab case'
# piRatio = 'camel case'
# Piratio = 'Pascal case'
# print(pi_ratio)
#
# print = 12
# print(my_value)

# value_a, value_b = 5, 'test'
# tmp = value_a
# value_a = value_b
# value_b = tmp
# print(value_a, value_b)

# value = '10.'
# print(value, type(value))
#
# # int, str, float - !!! нельзя делать именем переменной!!!!!!
#
# int_value = 1000
# print(int_value)
#
# my_value = input('Введи целое число: __')
# my_value = float(my_value)
# print(type(my_value), my_value * 10)

# int to float === float(10) = 10.0
# float to int === int(10.9) = 10
# int to str === str(10) = '10'
# float to str === str(3.14) = '3.14'
# str to int === int('10') = 10
# str to int === int('3.14') = error
# str to float === float('3.14') = 3.14
# str to float === float(abc) = error

# my_bool = 'qwe' in 'qwerty'
# print(type(my_bool), my_bool)

# Операторы сравнения:

# == равно
# != не равно
# > больше
# < меньше
# => больше либо равно
# <= меньше либо равно
# in есть ли в чем-то или нет

# Логические операторы:
# not, and, or
a = 'Hello, "A"'
b = a
c = 'Hello, "B"'
b = c
c = a
a = b
print(a)

my_value1 = 2
my_value2 = '4'

my_value1 = str(my_value1)
# my_value2 = int(my_value2)
print(my_value1 + my_value2)

my_value = 7
my_bool1 = my_value % 3 == 0
my_bool2 = my_value % 2 == 0
print(not my_bool1 and not my_bool2)


