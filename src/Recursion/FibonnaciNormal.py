"""
Implementación de cálculo de número fibonnaci normal
"""


def fibonnaci(num):
    memory = [0, 1]

    for i in range(1, num):
        memory.append(memory[i - 1] + memory[i])

    return memory[-1]


for i in range(0, 100):
    print("{0} fibonnaci number is {1}".format(i, fibonnaci(i)))
