print('1)-----------------------------------------------')
my_int = 102521902016
zero_count = str(my_int).count('0')
print(zero_count)
#####################################################
print('2)-----------------------------------------------')
my_int = 100201000000000
my_str = str(my_int)
my_str_reversed = str(int(my_str[::-1]))
zero_count = len(my_str) - len(my_str_reversed)
print(zero_count)
#####################################################
print('3)-----------------------------------------------')
my_list_1 = ['a', 'b', 2, 'd', ['qwe', 124]]
my_list_2 = ['asf', 24, 'z', 'kl', 88, 214.421]
result = []
# Я посчитал, что "Элементы на чётных местах" из условия - это элементы с чётными индексами
for index, symbol in enumerate(my_list_1):
    if not index % 2:
        result.append(symbol)
for index, symbol in enumerate(my_list_2):
    if index % 2:
        result.append(symbol)
print(result)
#####################################################
print('4)-----------------------------------------------')
my_list = [23, 326, 23, 45, 'qwr', [3.14, 'avs']]
first_elem = my_list.pop(0)
new_list = my_list
new_list.append(first_elem)
print(new_list)
#####################################################
print('5)-----------------------------------------------')
my_list = [23, 326, 23, 45, 'qwr', [3.14, 'avs']]
my_list.append(my_list.pop(0))
print(my_list)
#####################################################
print('6)-----------------------------------------------')
my_str = '164 больше чем 115 но меньше чем 221'
my_list = my_str.split()
print(my_list)
numbers_list = []
for index in my_list:
    if index.isdigit():
        numbers_list.append(int(index))
print(numbers_list)
numbers_sum = sum(numbers_list)
print(numbers_sum)
#####################################################
print('7)-----------------------------------------------')
my_str = 'My long string'
l_limit = 'o'
r_limit = 'g'
l_limit_index = my_str.find(l_limit)
r_limit_index = my_str.rfind(r_limit)
sub_str = my_str[l_limit_index + 1: r_limit_index]
print(sub_str)
#####################################################
print('8)-----------------------------------------------')
my_str = 'qwertyqwertyqwertyu'
my_list = []
for index in range(0, len(my_str), 2):
    sub_str = my_str[index:index+2]
    if len(sub_str) == 2:
        my_list.append(sub_str)
    else:
        sub_str = sub_str+'_'
        my_list.append(sub_str)
print(my_list)
#####################################################
print('9)-----------------------------------------------')
my_list = [2, 4, 1, 5, 3, 9, 0, 7, 21, 12521, 12, 21, 4, 15]
new_list = []
final_list = []
for index in range(len(my_list)):
    if index < len(my_list) - 2:
        sub_list = my_list[index:index+3]
        new_list.append(sub_list)
for index in range(len(new_list)):
    sub_list = new_list[index]
    if sub_list[1] > sub_list[0] + sub_list[2]:
        final_list.append(sub_list[1])
result = len(final_list)
print(final_list)
print(result)
