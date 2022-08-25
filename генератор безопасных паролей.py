from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exepted = ['i', 'l', '1', 'L', 'o', '0', 'O']
# контейнер для рандомных элементов из списка пароля на вывод пользователю
chars = ''

count_pas = input('Сколько нужно паролей?\n ')
len_pas = input('Какая длина пароля\n ')
# Основной список символов из которых будет состоять пароль(ли)
set_pass = []

digit_pass = input('Включать ли цифры 0123456789? да/нет\n ').lower()
if digit_pass == 'да':
    for i in range(len(digits)):
        set_pass.append(digits[i])

char_upper = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? да/нет\n ').lower()
if char_upper == 'да':
    for i in range(len(uppercase_letters)):
        set_pass.append(uppercase_letters[i])

char_lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? да/нет\n ').lower()
if char_lower == 'да':
    for i in range(len(lowercase_letters)):
        set_pass.append(lowercase_letters[i])

punct_pass = input('Включать ли символы !#$%&*+-=?@^_? да/нет\n ').lower()
if punct_pass == 'да':
    for i in range(len(punctuation)):
        set_pass.append(punctuation[i])

excep_pass = input('Исключать ли неоднозначные символы il1Lo0O? да/нет\n ').lower()
if excep_pass == 'да':
    for i in range(len(exepted)):
        if exepted[i] in set_pass:
            set_pass.remove(exepted[i])
        
# Генератор паролей
def generate_password(length, chars):
    chars = sample(set_pass, int(len_pas))
    return ''.join(chars)
# кол-во паролей
for i in range(int(count_pas)):
    print(generate_password(len_pas, set_pass))
            