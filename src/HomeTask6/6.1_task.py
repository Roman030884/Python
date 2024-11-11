import numpy as np
from functools import reduce
from operator import mul

# ДЗ. Вывести на экран произведение чисел от -10 до 7
# 1 вариант (ноль не исключен)

number_list1 = range(-10, 8, 1)
print(list(number_list1))
result1 = reduce(mul, list(number_list1))
print('Result1: ', result1)

# 2 вариант (ноль  исключен)
number_list2 = [i for i in range(-10, 8, 1)
                if i != 0]
print(number_list2)
result2 = np.prod(np.array(number_list2))
print('Result2: ', result2)
