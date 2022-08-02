# Interpretación de algoritmo de ordenamiento por burbuja


def bubble_sort(data):
    length = len(data)

    for i in range(length):
        for j in range(length-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data


if __name__ == '__main__':
    test_arr = [64, 25, 12, 22, 11]
    print("Original array: ", test_arr)

    test_arr = bubble_sort(test_arr)
    print("Array sorted: ", test_arr)