# Sobrecarga de operaciones

class Overloader:
    def __int__(self, value):
        self.value = value

    def __add__(self, other):
        self.value += other.value

    def __sub__(self, other):
        self.value -= other.value

    def __mul__(self, other):
        self.value *= other.value

    def __truediv__(self, other):
        self.value /= other.value

    def __floordiv__(self, other):
        self.value //= other.value

    def __mod__(self, other):
        self.value %= other.value

    def __pow__(self, power, modulo=None):
        self.value **= power

    def __rshift__(self, other):
        self.value >>= other.value

    def __lshift__(self, other):
        self.value <<= other.value

    def __and__(self, other):
        self.value &= other

    def __or__(self, other):
        self.value |= other.value

