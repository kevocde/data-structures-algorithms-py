# Implementación de algoritmo de ordenamiento por insersión

def insertion_sort(data):
    for i in range(1, len(data)):
        value = data[i]
        j = i - 1

        while j >= 0 and value < data[j]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = value

    return data


if __name__ == '__main__':
    test_arr = [64, 25, 12, 22, 11]
    print("Original array: ", test_arr)

    test_arr = insertion_sort(test_arr)
    print("Array sorted: ", test_arr)
