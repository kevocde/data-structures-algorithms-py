# Implementación de algoritmo de ordenamiento tipo shell

def shell_short(data):
    gap = len(data)

    while gap > 0:
        i = 0
        j = gap

        while j < len(data):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

            i += 1
            j += 1

            k = i
            while (k - gap) > -1:
                if data[k - gap] > data[k]:
                    data[k - gap], data[k] = data[k], data[k - gap]

                k -= 1

        gap //= 2

    return data

if __name__ == '__main__':
    test_arr = [64, 25, 12, 22, 11]
    print("Original array: ", test_arr)

    test_arr = shell_short(test_arr)
    print("Array sorted: ", test_arr)