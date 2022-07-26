from collections import deque
from queue import Queue

""" Test de operaciones básicas con queue (Colas) """
queue = []

# append() función para añadir un elemento en la queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# pop() función para sacar un elemento de la queue, cómo es de conportamiento FIFO obtendrá el primer elemento añadido
print("\nElements popped from queue:")
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after elements are popped:")
print(queue)

""" Implementación usando la librería estandar """
# Inicializando
queue = deque()

# Añadiendo elementos
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removiendo elementos de la cola
print("\nElementos dequeued from the queue")
print(queue.popleft())
print(queue.popleft())

print("\nQueue after removing elementos")
print(queue)

""" Implementación usando librería estandar Queue """
# Inicialización
queue = Queue(maxsize=3)

# qsize() retorna el tamaño de la cola en el momento
print(queue.qsize())

# Añadiendo elementos a la cola
queue.put('a')
queue.put('b')
queue.put('c')

# Retorna un booleano verdadero si la cola está llena
print("\nFull: ", queue.full())

# Eliminando elementos de la cola
print("\nElementos sacados de la cola")
print(queue.get())
print(queue.get())
print(queue.get())

# Retorna un booleano verdadero si la cola está vacía
print("\nEmpty: ", queue.empty())

queue.put(1)
print("\nEmpty: ", queue.empty())
print("Full: ", queue.empty())
