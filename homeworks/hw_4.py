print('1)-----------------------------------------------')
my_list = [0, 1, 2, 3, 4, 5, 125, 361361, 1242, -125125, 0]
for value in my_list:
    if value > 100:
        print(value)
#####################################################
print('2)-----------------------------------------------')
my_list = [0, 1, 2, 3, 4, 5, 125, 361361, 1242, -125125, 0]
my_results = []
for value in my_list:
    if value > 100:
        my_results.append(value)
print(my_results)
#####################################################
print('3)-----------------------------------------------')
my_list = [0, 1, 2, 3, 4, 5, 125, 361361, 1242, -125125]
if len(my_list) < 2:
    my_list.append(0)
    print(my_list)
else:
    last_two_sum = my_list[-1] + my_list[-2]
    my_list.append(last_two_sum)
    print(my_list)
#####################################################
print('4)-----------------------------------------------')
value = False
while not value:
    value = input('Enter a float value except zero')
    if '.' in value:
        try:
            value = float(value)
            result = value ** -1
            print(result)
            value = True
        except ZeroDivisionError:
            print('You can not enter a zero')
        except ValueError:
            print('It is not a float, try again')
            value = False

    else:
        print('It is not a float value, try again')
        value = False
#####################################################
print('5)-----------------------------------------------')
my_string = '0123456789'
my_list = []
for value in my_string:
    for new_value in my_string:
        my_list.append(int(value + new_value))
print(my_list)



