# Implementación de algoritmo de ordenamiento por mezcla

def merge_sort(data):
    if len(data) > 1:
        middle = len(data) // 2
        left_arr = data[:middle]
        right_arr = data[middle:]

        left_arr = merge_sort(left_arr)
        right_arr = merge_sort(right_arr)

        i = j = k = 0

        # compara los items entre si de cada mitad para determinar el más pequeño
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                data[k] = left_arr[i]
                i += 1
            else:
                data[k] = right_arr[j]
                j += 1

            k += 1

        # Si llegara a faltar partes de cada mitad por recorrer se realizará el barrido para añadir esos elementos
        # faltantes
        while i < len(left_arr):
            data[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            data[k] = right_arr[j]
            j += 1
            k += 1

    return data


if __name__ == '__main__':
    test_arr = [64, 25, 12, 22, 11]
    print("Original array: ", test_arr)

    test_arr = merge_sort(test_arr)
    print("Array sorted: ", test_arr)