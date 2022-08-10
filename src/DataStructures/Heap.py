""" Prueba de implementación de "Heap" montón y sus operaciones """
import heapq

li = [5, 7, 9, 1, 3]

# Usuando heapify para compertir una lista en un montón
heapq.heapify(li)

# Imprimiendo el montón creado
print("The created heap is: ", end="")
print(list(li))

# Usando heappush() para añadir elementos en el montón
heapq.heappush(li, 4)

# Imprimiendo el montón modificado
print("The modified heap after push is: ", end="")
print(list(li))

# Usando heappop() para sacar el elementos más pequeño
print("The popped and smallest elements is: ", end="")
print(heapq.heappop(li))