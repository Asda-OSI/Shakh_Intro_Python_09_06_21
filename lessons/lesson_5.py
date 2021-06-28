# my_str = 'blablacarblablacar'
# my_symbol = 'bla'
#
# my_symbol_count = my_str.count('bla')
# print(my_symbol_count)
#
# res_msg = f'{my_symbol}\n' * my_symbol_count
# print(res_msg.strip())
# for _ in range(my_symbol_count):
#     print(my_symbol)

# my_str = 'bla Bla car'
# my_str = my_str.lower()
# symbols_heap = []
# for symbol in my_str:
#     if symbol not in symbols_heap:
#         symbols_heap.append(symbol)
# res_len = len(symbols_heap)
# print(res_len)


# my_str = 'qwerty'
# my_list = []

# for index in range(len(my_str)):
#     if not index % 2:
#         symbol = my_str[index]
#         my_list.append(symbol)

# for value in enumerate(my_str): # распаковка
#     print(value)

# for index, symbol in enumerate(my_str):
#     if not index % 2:
#         my_list.append(symbol)
#
#
# print(my_list)

# my_str = 'qwerty'
# str_index = [3, 2, 5, 1, 0, 5, 0, 3, 2, 1, 0, 4, 2]
# my_list = []
# for index in str_index:
#     symbol = my_str[index]
#     my_list.append(symbol)
# print(my_list)

# my_number = 1259219521956188215821940124214
# digit_count = len(str(my_number))
# print(digit_count)

# my_number = 12431512421412315231523414124231432161231  # ord() // shr()
#
# number_str = str(my_number)
# max_symbol = max(number_str)
# print(max_symbol)
#
# test_list = ['1', "2", "3", '4']
# print(max(test_list))

# my_number = 12431512421412315231523414124231432161231
#
# number_str = str(my_number)
# new_number_str = number_str[::-1]
# new_number_int = int(new_number_str)
# print(new_number_int)


# my_list = [1, 2, 5, 3, -8, 9, 124]
# my_str = 'qwerty'
# sorted_list = sorted(my_str)
# print(sorted_list)

number = 121360132693207231719326023

number_str = str(number)
sorted_number_symbols_list = sorted(number_str, reverse= True)
new_number_str = ''.join(sorted_number_symbols_list)
new_number = int(new_number_str)
print(new_number)
