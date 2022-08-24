import random
rand_digit = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
def is_valid(num):
    return num.isdigit() and 1 < int(num) <=100
num = input()
print(is_valid(num))