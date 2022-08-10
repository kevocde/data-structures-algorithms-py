# Muestra del funcionamiento del operador ternario / expresiones condicionales en python

# Método simple para usar un operador terneario
a, b = 10, 20
num_min = a if a < b else b  # simple ternary use
print(num_min)

# Método directo usando tuplas, diccionarios y funciones lambda
print((b, a)[a < b])  # a < b returns the one index and the other way around

print({True: a, False: b}[a < b])  # a < b returns the True key and the other way around

print((lambda: b, lambda: a)[a < b]())  # a < b returns the lambda function and later is called.

# Anidado de operadores ternarios
print("A and B are equal" if a == b else "A is greater that B" if a > b else "B is greater that A")

# Otras formas
print(a, "is greater") if a > b else print(b, "is greater")