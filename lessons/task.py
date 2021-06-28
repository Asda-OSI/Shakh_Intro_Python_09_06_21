tmp_value = 5

go_game = True

condition = 'Введите число от 1 до 10:'
while go_game:
    try:
        your_value = int(input(condition))
        if your_value < tmp_value:
            condition = 'Попробуй больше:'
        elif your_value > tmp_value:
            condition = 'Попробуй меньше:'
        else:
            go_game = False
            print('Хорош!')
    except ValueError:
        condition = 'Введите число от 1 до 10:'
