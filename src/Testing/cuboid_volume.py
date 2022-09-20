def cuboid_volume(length):
    if type(length) not in [int, float]:
        raise TypeError

    return length**3
