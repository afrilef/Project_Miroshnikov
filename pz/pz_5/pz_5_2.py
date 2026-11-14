# Вариант №17
# Описать функцию PowerA3(A, B), вычисляющую третью степень числа A и
# возвращающую ее в переменную B (A — входной, B — выходной параметр; оба
# параметра являются вещественными). С помощью этой функции найти третьи
# степени пяти данных чисел.

def PowerA3(A):
    B = A ** 3 #в третью степень
    return B

count = 1 #счетчик
while count <= 5:
    number = input('Введите число: ')  # Ввод числа
    while not type(number) == float:  # проверка типа
        try:
            number = float(number)
        except ValueError:
            print('Ошибка, введите число! ')
            number = input('Введите число: ')
    result = PowerA3(number) #в result записывает число в степени
    print('Третья степень:', result) #выводит
    count += 1