# 3. Найти количество кратных 10 (10, 20, 30 ...) чисел в списке

number_list = range(10, 112, 5)
print(list(number_list))
counter = 0
for number in number_list:
    if (number % 10) == 0:
        counter += 1
print('the number of multiples', counter)
