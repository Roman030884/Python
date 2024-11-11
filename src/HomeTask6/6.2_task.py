# 2. Найти сумму чётных чисел от N до M, включая N и M,
# где N и M вводятся через input().
# Учесть условие когда первое число больше второго


number_1 = int(input('enter a first number: '))
number_2 = int(input('enter a second number: '))

if number_1 > number_2 and number_1 % 2 == 0 and number_2 % 2 == 0:
    print('Summa of numbers: ', number_1 + number_2)

else:
    print('The first number less second or one or both of numbers are odd')
