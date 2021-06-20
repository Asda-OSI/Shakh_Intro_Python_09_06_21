# 1
value = 5
new_value = value / 2 if value < 100 else -value
print(f'1) {new_value}')
print('--------------------------------------------')
#####################################################
# 2
value = 15125
new_value = 1 if value < 100 else 0
print(f'2) {new_value}')
print('--------------------------------------------')
#####################################################
# 3
value = 12
new_value = True if value < 100 else False
print(f'3) {new_value}')
print('--------------------------------------------')
#####################################################
# 4
my_str = 'My String'
my_str = my_str.upper()
print(f'4) {my_str}')
print('--------------------------------------------')
#####################################################
# 5
my_str = 'My String'
my_str = my_str.lower()
print(f'5) {my_str}')
print('--------------------------------------------')
#####################################################
# 6
my_str = 'Str'
my_str = my_str * 2 if len(my_str) < 5 else my_str
print(f'6) {my_str}')
print('--------------------------------------------')
#####################################################
# 7
my_str = 'Str'
my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(f'7) {my_str}')

