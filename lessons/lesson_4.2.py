# count = 10
# while count > 0:
#     # count += 1  # увеличение на 1
#     count -= 1  # уменьшение на 1
#     print(f'count = {count}')
# print('The end')




## ДЗ* давать подсказки типа: "Попробуй больше", "Попробуй меньше"


# result = []
# test_str = 'qwertyYEoOA!3@$@)%'
#
# for symbol in test_str:
#     if symbol.lower() not in 'euioay' and symbol.isalpha():
#         result.append(symbol)
# print(result)
#
# # list_str = list(test_str)
# # print(list_str)
#
# joint_str = '___'.join(result)
# print(joint_str)
#
# list_str = split(join_str)

# tuple - кортеж - неизменяемый тип
# list - список - изменяемый тип

# my_tuple = (1, 2, 'qwe', (-1, 0), None)
# # print(type(my_tuple), my_tuple)
#
# my_list = [1, 2, 'qwe', (-1, 0), None]
# #
# index = -2
# my_list[index] = 3
#
# value_tuple = my_tuple[index]
# value_list = my_list[index]
# print(value_tuple, value_list)
# print(type(my_tuple), type(my_list))
# срезы как в списках

# my_tuple = list(my_tuple)
# print(type(my_tuple), my_tuple)

# Методы: что-то возвращают и ничего не возвращают
# new_list = []
#
# some_value = new_list.append('first')
# new_list.append('second')
# new_list.append([1, 3, 5])
# last_value = new_list.pop()
# print(new_list)
# print(last_value, some_value)
# стек