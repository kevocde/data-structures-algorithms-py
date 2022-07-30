# Implementación de búsqueda lineal en python


def search(needle, haystack):
    for idx, value in enumerate(haystack):
        if value == needle:
            return idx
    return -1


# Impar list numbers
haystack_1 = list(range(1, 200, 2))
if search(196, haystack_1) != -1:
    print("196 is in the list")
else:
    print("196 isn't in the list")

# Par list numbers
haystack_2 = map(lambda value: value - 1, haystack_1)
if search(196, haystack_2) != -1:
    print("196 is in the list")
else:
    print("196 isn't in the list")