"""
El patrón de diseño Bridge, permite reducir la complejidad de añadir mas y mas caraterísticas y por ende lógica al
código ya existente.
"""
import math
from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def pain(self):
        pass


class Shape(ABC):
    def __init__(self):
        self._color = None

    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass

    def get_color(self) -> Color:
        return self._color

    def set_color(self, value: Color):
        self._color = value


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self._radius = radius

    def get_area(self) -> float:
        return math.pi * self._radius ** 2

    def get_perimeter(self) -> float:
        return math.pi * self._radius * 2


class Red(Color):
    def pain(self):
        return 'rgb(255, 0, 0)'


if __name__ == '__main__':
    print("Client needs a circule")
    circule = Circle(12.4)

    print("Now, the client needs a circulo but red")
    red = Red()
    circule.set_color(red)

    print(f"Now, the circule has a perimeter of {circule.get_perimeter()} and its color's {circule.get_color().pain()}")
