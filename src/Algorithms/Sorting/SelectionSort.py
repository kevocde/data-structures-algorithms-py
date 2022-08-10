# Interpretación del algoritmo de ordenamiento por selección


def sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

    return data


if __name__ == '__main__':
    test_arr = [64, 25, 12, 22, 11]
    print("Original array: ", test_arr)

    test_arr = sort(test_arr)
    print("Array sorted: ", test_arr)
