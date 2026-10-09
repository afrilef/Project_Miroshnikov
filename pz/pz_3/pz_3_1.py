# Вариант 17.
# 1. Дано целое положительное число. Проверить истинность высказывания: «Данное число является четным двузначным».

number = input('Введите число: ')  # Ввод числа
while not type(number) == float:   # проверка типа
    try:
        number = float(number)
    except ValueError:
        print('Ошибка, введите число! ')
        number = input('Введите число: ')

if 10 <= number <= 99 and number % 2 == 0:  # условия истиности
    print('Истина')
else:
    print('Ложь')

