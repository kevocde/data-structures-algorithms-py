from pydoc import doc
import numpy as np

a = np.array([[1, 3, 5], [7, 9, 11], [13, 15, 18]])

# Hace una copia de la matriz, en una posición diferente de memoria
m = np.reshape(a, (3, 3))

# Añadiendo otra posición a la matriz
print("Adding Element")
m = np.append(m, [[20, 23, 25]], 0)
print(m)

# Eliminando una posición
m = np.delete(m, [1], 0)
print("Deleting Element")
print(m)