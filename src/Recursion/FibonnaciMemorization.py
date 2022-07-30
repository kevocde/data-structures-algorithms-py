"""
Implementación de cálculo de número fibonnaci por medio de memorización
"""


def fibonnaci(num, memory=None):
    if memory is None:
        memory = [None] * (num + 1)

    if memory[num] is not None:
        return memory[num]

    if num in [0, 1]:
        return num
    else:
        memory[num] = fibonnaci(num - 1, memory) + fibonnaci(num - 2, memory)
        return memory[num]


for i in range(0, 100):
    print("{0} fibonnaci number is {1}".format(i, fibonnaci(i)))
