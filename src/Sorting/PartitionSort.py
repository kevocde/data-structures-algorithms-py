# Interpretación de algoritmo de ordenamiento rápido (quick sort)


def get_partition(data, start, end):
    pivot_idx = start
    pivot = data[start]

    while start < end:
        while start < len(data) and data[start] <= pivot:
            start += 1

        while data[end] > pivot:
            end -= 1

        if start < end:
            data[start], data[end] = data[end], data[start]

    data[end], data[pivot_idx] = data[pivot_idx], data[end]

    return [end, data]


def quick_sort(data, start=0, end=None):
    if end is None:
        end = len(data) - 1

    if start < end:
        partition, data = get_partition(data, start, end)
        print(partition, data)

        data = quick_sort(data, start, partition - 1)
        data = quick_sort(data, partition + 1, end)

    return data


if __name__ == '__main__':
    test_arr = [64, 25, 12, 22, 11]
    print("Original array: ", test_arr)

    test_arr = quick_sort(test_arr)
    print("Array sorted: ", test_arr)