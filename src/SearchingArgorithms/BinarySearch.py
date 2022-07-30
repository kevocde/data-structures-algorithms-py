# Implementación de algoritmo de búsqueda binaria


def binary_search(needle, haystack):
    length = len(haystack) - 1

    if length >= 0:
        middle = length // 2  # Obtenemos la llave del valor medio

        if haystack[middle] == needle:  # Si el valor es el de la mitad
            return [haystack[middle]]
        elif haystack[middle] > needle:  # Si el valor es menor que la mitad se recorta el arreglo de 0 hasta la
            # mitad menos 1
            return binary_search(needle, haystack[0:(middle - 1)])
        else:  # Si el valor es mayor a la mitad se recorta desde la mitad más 1 hasta el final del arreglo
            return binary_search(needle, haystack[(middle + 1): length])
    else:
        return []


haystack_1 = [2, 3, 4, 10, 40]
needle_value = 10

result = binary_search(needle_value, haystack_1)
if not len(result):
    print("Element isn't present in the array")
else:
    print("Element present in the array")