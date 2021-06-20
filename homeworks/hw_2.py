int_value = input('Please enter an integer')
try:
    int(int_value)
except ValueError:
    print('It is not an integer')
else:
    print(int(int_value) * 2)
print('----------------------------------------')
##########################################################################################
float_value = input('Please enter a float value')
try:
    float(float_value)
except ValueError:
    print('It is not a float value')
else:
    print(float(float_value) * 2)
print('----------------------------------------')
##########################################################################################
str_value = input('Please enter a string value')
print(str_value * 2)
print('----------------------------------------')



