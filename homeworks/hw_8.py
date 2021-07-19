# TASK1
print('-----------------------------------TASK1---------------------------------------')
persons = [{'name': 'Anna', 'age': 15}, {'name': 'Kristopher', 'age': 45},
           {'name': 'Cris', 'age': 15}, {'name': 'Dave', 'age': 32},
           {'name': 'Ivan', 'age': 45}, {'name': 'Kate', 'age': 18}]

ages = []
youngest_persons = []
oldest_persons = []
for person in persons:
    ages.append(person.get('age'))

for person in persons:
    if person['age'] == min(ages):
        youngest_persons.append(person['name'])
    if person['age'] == max(ages):
        oldest_persons.append(person['name'])

print(f'а) Youngest: {", ".join(youngest_persons)}')  # a)
print(f'б) Oldest: {", ".join(oldest_persons)}')  # б)
average_age = sum(ages) / len(ages)  # в)
print(f'в) Average age: {average_age}')

# TASK2
print('-----------------------------------TASK2---------------------------------------')
my_dict_1 = {
    'unique_key_1': 'unique_value_1',
    'key_1': 'value_1',
    'key_2': 'value_2',
    'unique_key_2': 'unique_value_2',
    'unique_key_3': 'unique_value_3',
}

my_dict_2 = {
    'unique_key_4': 'unique_value_4',
    'key_1': 'value_3',
    'key_2': 'value_2',
    'unique_key_5': 'unique_value_5',
    'unique_key_6': 'unique_value_6',
}

my_dict_1_keys = [key_1 for key_1 in my_dict_1.keys()]
my_dict_2_keys = [key_2 for key_2 in my_dict_2.keys()]

# a)
my_dict_1_keys_set = set(my_dict_1_keys)
my_dict_2_keys_set = set(my_dict_2_keys)
both_dicts_keys = list(my_dict_1_keys_set.intersection(my_dict_2_keys_set))
print(f'а) Keys in both dictionaries: {", ".join(both_dicts_keys)}')

# б)
unique_first_dict_keys = list(my_dict_1_keys_set.difference(my_dict_2_keys_set))
print(f'б) Keys that are in the first dict but not in the second: {", ".join(unique_first_dict_keys)}')

# в)
new_dict = {}
for unique_first_dict_key in unique_first_dict_keys:
    new_dict[unique_first_dict_key] = my_dict_1[unique_first_dict_key]
print(f'в) Dict with unique keys from first dict: {new_dict}')

# г)
result_dict = {}
value_list = []

# Способ 1
keys_union = my_dict_1_keys_set.union(my_dict_2_keys_set)
new_list = []
for key_from_union in keys_union:
    if key_from_union in my_dict_1_keys and key_from_union in my_dict_2_keys:
        result_dict[key_from_union] = [my_dict_1[key_from_union], my_dict_2[key_from_union]]
    elif key_from_union in my_dict_1_keys:
        result_dict[key_from_union] = my_dict_1[key_from_union]
    else:
        result_dict[key_from_union] = my_dict_2[key_from_union]


# Способ 2
# keys_list = my_dict_1_keys + my_dict_2_keys
#
# for key in keys_list:
#     if keys_list.count(key) == 1:
#         if key in my_dict_1_keys:
#             result_dict[key] = my_dict_1[key]
#         else:
#             result_dict[key] = my_dict_2[key]
#     else:
#         # value_list.extend([my_dict_1[key], my_dict_2[key]])
#         result_dict[key] = [my_dict_1[key], my_dict_2[key]]


# Способ 3
# for key, value in my_dict_1.items():
#     if key in my_dict_2_keys:
#         value_list.append(value)
#         value_list.append(my_dict_2[key])
#         result_dict[key] = value_list
#         value_list = []
#     else:
#         result_dict[key] = value
# for key_2, value_2 in my_dict_2.items():
#     if key_2 not in result_dict.keys():
#         result_dict[key_2] = value_2


# Result г)
print(f'г) Dict with keys and values from both dicts: {result_dict}')


