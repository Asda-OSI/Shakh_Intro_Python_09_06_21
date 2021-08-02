# with open('lesson_10.py', 'r') as py_file:
#     data = py_file.readlines()
#
# print(data, type(data))
#
# data.append('# FINISH')
#
# with open('lesson_10_new.py', 'w') as py_file:
#     py_file.writelines(data)

with open('lesson_10.py', 'r') as py_file:
    data = py_file.readlines()

for line in data:
    print(line.split('\t'))
