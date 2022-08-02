# Implementación de algoritmo de búsqueda ternaria


def termary_search(needle, haystack, start=0, length=None):
    if length is None:
        length = len(haystack) - 1

    if length >= start:
        middle_button = start + (length - start) // 3
        middle_top = length - (length - start) // 3

        if haystack[middle_button] == needle:
            return middle_button

        if haystack[middle_top] == needle:
            return middle_top

        if needle < haystack[middle_button]:
            return termary_search(needle, haystack, start, middle_button - 1)
        elif needle > haystack[middle_top]:
            return termary_search(needle, haystack, middle_top + 1, length)
        else:
            return termary_search(needle, haystack, middle_button + 1, middle_top - 1)
    else:
        return -1


haystack_1 = [1, 2, 4, 8, 23, 24, 29, 30, 33, 34, 39, 42, 48, 48, 69, 74, 74, 75, 79, 80, 82, 88, 90, 92, 96, 97, 100, 101, 104, 107, 108, 111, 114, 125, 128, 130, 134, 144, 150, 151, 155, 156, 164, 171, 172, 174, 177, 177, 179, 184, 189, 191, 191, 195, 199, 201, 231, 234, 235, 240, 241, 244, 246, 246, 250, 254, 262, 263, 272, 273, 278, 303, 308, 321, 321, 322, 326, 335, 347, 352, 364, 364, 366, 368, 376, 376, 386, 392, 392, 393, 396, 402, 403, 407, 419, 421, 422, 441, 445, 446, 453, 466, 468, 473, 477, 500, 503, 508, 515, 526, 532, 533, 549, 557, 562, 577, 580, 588, 595, 613, 613, 615, 620, 628, 630, 631, 642, 646, 646, 649, 651, 653, 664, 664, 668, 669, 671, 672, 680, 688, 694, 698, 702, 711, 718, 718, 722, 723, 725, 732, 743, 750, 761, 776, 782, 795, 797, 799, 801, 801, 808, 823, 829, 830, 835, 841, 847, 849, 857, 864, 867, 869, 871, 872, 874, 878, 880, 882, 888, 889, 893, 895, 897, 899, 905, 906, 910, 912, 936, 937, 940, 957, 960, 969, 972, 976, 978, 982, 989, 991, 994, 994, 1000, 1000, 1002, 1002, 1004, 1017, 1029, 1035, 1044, 1050, 1066, 1070, 1071, 1072, 1072, 1089, 1101, 1104, 1105, 1114, 1129, 1132, 1133, 1143, 1146, 1151, 1151, 1153, 1167, 1168, 1170, 1175, 1178, 1181, 1182, 1186, 1191, 1200, 1213, 1218, 1230, 1239, 1248, 1254, 1260, 1264, 1270, 1272, 1278, 1279, 1282, 1283, 1283, 1284, 1297, 1300, 1302, 1302, 1305, 1318, 1318, 1320, 1335, 1339, 1349, 1356, 1357, 1358, 1369, 1371, 1375, 1377, 1392, 1393, 1402, 1406, 1416, 1416, 1423, 1424, 1440, 1440, 1462, 1464, 1466, 1466, 1467, 1469, 1469, 1473, 1480, 1480, 1481, 1491, 1495, 1496, 1500, 1502, 1504, 1509, 1513, 1515, 1516, 1523, 1523, 1535, 1537, 1544, 1548, 1555, 1557, 1558, 1559, 1562, 1568, 1579, 1580, 1586, 1595, 1600, 1603, 1617, 1622, 1627, 1631, 1634, 1652, 1660, 1666, 1666, 1668, 1676, 1676, 1680, 1682, 1685, 1689, 1693, 1697, 1701, 1701, 1703, 1703, 1708, 1717, 1721, 1726, 1733, 1743, 1744, 1745, 1745, 1746, 1750, 1761, 1771, 1790, 1798, 1801, 1802, 1806, 1826, 1828, 1831, 1833, 1836, 1836, 1839, 1843, 1844, 1847, 1856, 1858, 1858, 1879, 1895, 1896, 1901, 1908, 1919, 1923, 1931, 1934, 1936, 1940, 1943, 1945, 1952, 1953, 1965, 1966, 1966, 1983, 1984, 1986, 1990, 1992, 1999]
needle_value = 111

result = termary_search(needle_value, haystack_1)
if result == -1:
    print("Element isn't present in the array")
else:
    print("Element present in the array in the position: %d" % result)