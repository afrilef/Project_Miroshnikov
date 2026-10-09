# вариант №17
# Дано трехзначное число. Вывести число, полученное при прочтении исходного числа справа налево

try:
   chislo = int(input('введите трехзначное число: ')) # ввод числа

   edinichki = chislo % 10 # где единицы
   desatki = (chislo // 10) % 10 #где десятки
   sotni = chislo // 100 #где сотни

   obratnoe_chislo = edinichki * 100 + desatki * 10 + sotni # обратная запись

   print('результат:', obratnoe_chislo) # вывод обратного числа
except ValueError: 
   print('ошибка, введите число') #при некорректном вводе
  
