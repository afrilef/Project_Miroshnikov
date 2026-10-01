chislo = int(input('введите трехзначное число: '))

edinichki = chislo % 10
desatki = (chislo // 10) % 10
sotni = chislo // 100

obratnoe_chislo = edinichki * 100 + desatki * 10 + sotni

print('результат:', obratnoe_chislo)