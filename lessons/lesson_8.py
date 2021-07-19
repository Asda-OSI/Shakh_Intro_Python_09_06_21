# # методы словарей
#
# symbols = {symbol: ord(symbol) for symbol in 'eyuio'}
# print(symbols)
#
#
persons = {'John': 12, 'Jack': 34, 'Anna': 27}
# # print(persons['Anna'])
#
persons['Jackob'] = 59
# persons['John'] = print(persons['John'])
# # persons.clear()
# # persons = {}
#
# print(persons.get('Vova', -1))
#
# result = 'Anna' in persons  # in проверяет только ключи!!
# print(result)
#
#
# key = 'Anna'
# # if key not in persons:
# #     persons[key] = 41
# #
# # print(persons)
# #
# for key in persons:
#     print(key, persons[key])
#
# for key, value in persons.items():
#     print(key, value)
#
# # print(type(persons.keys()), persons.keys())
# # print(type(persons.values()), persons.values())
#
# max_age = max(persons.values())
# print(max_age)
#

# print('\m\\a\\x\_\\a\\g\\e')
#
# value = input()
# print(value)
for key in persons:
    print(key, persons[key])
value = persons.pop('Jackob')
print(value)
for key, value in persons.items():
    print(key, value)