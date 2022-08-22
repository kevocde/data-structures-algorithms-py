from enum import Enum


class Color(Enum):
    YELLOW = 'FFF8DC'
    BLUE = '008000'
    RED = 'FF0000'


print(Color)
print(type(Color), type(Color.RED))
print(Color.RED.value)
