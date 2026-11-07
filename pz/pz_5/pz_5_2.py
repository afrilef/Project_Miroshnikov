# Вариант №17
# Описать функцию PowerA3(A, B), вычисляющую третью степень числа A и
# возвращающую ее в переменную B (A — входной, B — выходной параметр; оба
# параметра являются вещественными). С помощью этой функции найти третьи
# степени пяти данных чисел.

def PowerA3(A, B = 0.0):
    B = A ** 3
    return B

count = 1
while count <= 5:
    number = input('Введите число: ')  # Ввод числа
    while not type(number) == float:  # проверка типа
        try:
            number = float(number)
        except ValueError:
            print('Ошибка, введите число! ')
            number = input('Введите число: ')
    result = 0.0
    result = PowerA3(number, result)
    print('Третья степень:', result)
    count += 1