tmp_value = 5

go_game = True

condition = 'Введите число от 1 до 10:'
while go_game:
    your_value = input(condition)
    try:
        your_value = int(your_value)
    except ValueError:
        your_value = ''
        print('Not a number')

    if your_value == '':
        condition = 'Попробуй ещё:'
    elif your_value < tmp_value:
        condition = 'Попробуй больше:'
    elif your_value > tmp_value:
        condition = 'Попробуй меньше:'
    else:
        go_game = False
        print('Хорош!')