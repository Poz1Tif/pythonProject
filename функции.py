import random
def start_game():
    count = 0
    n = int(input('Укажите максимально угадываемое число: '))
    rand_digit = random.randint(1, n)
    print('Добро пожаловать в числовую угадайку')
    def is_valid(num):
        return num.isdigit() and 1 < int(num) <= n
    print('Введите число от 1 до', n, ': ')
    num = input()
    while is_valid(num) == False:
        print('А может быть все-таки введем целое число от 1 до', n, '? ')
        print('Введите число от 1 до', n, ': ')
        num = input()
    else:
        num = int(num)
    while num != rand_digit:
        count += 1
        if num < rand_digit:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num > rand_digit:
            print('Ваше число больше загаданного, попробуйте еще разок')
        num = int(input())
    print('Вы угадали, поздравляем!')
    print('Вы потратили', count, 'попыток!')
    back = input('Желаете сыграть снова?\nВведите ДА или НЕТ ').lower()
    if back == 'да' or back == 'yes' or back == 'y' or back == 'д':
        return start_game()
    else:
        return print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
start_game()

