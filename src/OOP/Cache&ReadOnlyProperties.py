import math


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius must be positive')

        if value != self._radius:
            self._radius = value
            self._area = None

    def area(self):
        if self._area is None:
            self._area = math.pi * self.radius ** 2

        return self._area


# Ahora cada vez que se cree un objeto círculo y se llame a la propiedad área la primera vez calculará
# pero si se vuelve a llamar esta no se recalculara, a menos que se cambie antes el radio.
me_circle = Circle(100)
print(me_circle.area())
print(me_circle.area())

me_circle.radius = 13
print(me_circle.area())
