"""
Prototype es un patrón de diseño creacional, que permite crear copias exactas de un determinado objecto, sin añadir más
dependencias.
"""
import copy


class Airplane:
    def __init__(self, passengers, payload):
        self._passengers = passengers
        self._payload = payload

    def __copy__(self):
        passengers = copy.copy(self._passengers)
        payload = copy.copy(self._payload)

        prototype = self.__class__(passengers, payload)
        prototype.__dict__.update(self.__dict__)

        return prototype

    def __deepcopy__(self, memodict=None):
        if not memodict:
            memodict = {}

        passengers = copy.deepcopy(self._passengers)
        payload = copy.deepcopy(self._payload)

        prototype = self.__class__(passengers, payload)
        prototype.__dict__ = copy.deepcopy(self.__dict__, memodict)

        return prototype


if __name__ == '__main__':
    original = Airplane(100, 10)
    first_copy = copy.copy(original)

    print(id(original), id(first_copy))
