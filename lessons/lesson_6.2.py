# множества set - не сохраняет порядок, все элементы уникальные

# my_list = [3, 10, 10, 2, 2, "2", 3, 3, 3, 3, 3, 3]
# my_list_unique = list(set(my_list)) - убирает дубли
# my_set = set(my_list)
# print(my_set)
# my_list_unique = list(my_set)
#
# print(my_list_unique)
# new_set = {1, 2, 3, 4, 54, 54}
# print(new_set)


# my_str = 'bla BLA car'
# my_str = my_str.lower()
# res_len = len(set(my_str))
# print(res_len)

# my_str = 'qqqqqqqqqqqqqwwwwwwwwwwweeeeeeeeeeeeeeeeeeeertyy'
# for symbol in set(my_str):
#     print(symbol, my_str.count(symbol))

# my_str_1 = 'qwerty'
# my_str_2 = 'qweasd'
# my_set_1 = set(my_str_1)
# my_set_2 = set(my_str_2)
#
# intersection = my_set_1.intersection(my_set_2)
# print(intersection)
#
# union = my_set_1.union(my_set_2)
# print(union)
#
# difference = my_set_1.difference(my_set_2)
# print(difference)

# словарь - dict не гарантирует сохранение порядка, все ключи уникальные
# ключи - любые неизменяемые объекты
# значения - любые объекты
# triangle = [[1, 1], [2, 3], [4, -2]]
# print(triangle[1][1])

key = (1, 2, 'qwe')
test_dict = {11: '12',
             '11': 12,
             key: 'test'}
print(test_dict[key])
triangle = {'A': {'x': 1, 'y': 1},
            'B': {'x': 2, 'y': 3},
            'C': {'x': 4, 'y': -2}}
print(triangle)
