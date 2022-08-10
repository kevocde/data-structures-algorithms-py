""" Test de operaciones básicas con stacks (pilas) """
stack = []

# append() función para añadir un elemento en el stack
stack.append('a')
stack.append('b')
stack.append('c')

print("Initial stack")
print(stack)

# pop() función para sacar un elemento del stack, cómo es de conportamiento LIFO obtendrá el último elemento añadido
print("\nElements popped from stack:")
print(stack.pop())
print(stack.pop())

print("\nStack after elements are popped:")
print(stack)
