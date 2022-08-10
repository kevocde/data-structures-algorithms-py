"""
Esta es una implementación de la secuencia de fibonnaci por medio de recursion tabulada.
"""

fact_list = {}


def factorial(num):
    if num == 1 or num <= 0:
        return 1
    elif num in fact_list:
        return fact_list[num]
    else:
        fact_list[num] = (num * factorial(num - 1))
        return fact_list[num]


for i in range(0, 201, 3):
    print("{0}! = {1}".format(i, factorial(i)))
