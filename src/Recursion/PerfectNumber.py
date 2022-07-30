"""
Este es un ejemplo de recursividad simple con la finalidad que hallar si un número dado es perfecto,
Fallas:
    * Al ser un algoritmo recursivo se verá números superiores a 1000 generan fallas de memoria
"""


def is_perfect_tool(num, counter=None):
    """Permite sumar las raices cuadradas de cada número hasta llegar al número objetivo"""
    counter = 2 if counter is None else counter

    if counter > num:
        return 1
    else:
        if (counter ** 2 <= num) and not (num % counter):
            result = ((num + counter ** 2) / counter)
        else:
            result = 0

        counter += 1
        return result + is_perfect_tool(num, counter)


def is_perfect(num):
    """Función primaria que se encarga de evaluar codicionales aparte"""
    return num != 1 and num == is_perfect_tool(num)


for i in range(500):
    if is_perfect(i):
        print("{} is a perfect number".format(i))
