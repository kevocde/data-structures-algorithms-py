"""
AbstractFactory es un patrón de diseño creacional, el cual resuelte tle preblema de crear
grupos de objetos (entidades), de un tipo o familia específicos sin especificar sus clases concretamente.

El siguiente es la implementación del patrón en una tienda de muebles:
    En la tienda de muebles se ofresen tan solo tres productos estrella, sillas, sofás, y mesas; cada uno de
    estos productos tienen tres variantes distintas, variante moderna, antigua y artdeco. El problema es que el almacén
    permite hacer el pedido por un sistema, pero al realizar el pedido muchas ocaciones se entregan los productos al
    cliente pero con distintos estilos, lo cual es feo. Por lo anterior es necesario que sin importar cuál de los trés
    productos escoja el cliente, el sistema solo pregunte una vez cuál es el estilo que requiere.
"""
from abc import ABC, abstractmethod


class Chair(ABC):
    """
    Clase Silla, esta clase define las particuridades de cualquiér silla.
    """
    @abstractmethod
    def sit(self) -> str:
        pass


class Sofa(Chair):
    """
    Clase Sofa, esta clase define las particularidades de cualquiér sofá.
    """
    pass


class Table(ABC):
    """
    Clase Mesa, esta clase define las particularidades de cualquiér mesa.
    """
    @abstractmethod
    def serve(self) -> str:
        pass


class FournitureFactory(ABC):
    @abstractmethod
    def createChair(self) -> Chair:
        pass

    @abstractmethod
    def createSofa(self) -> Sofa:
        pass

    @abstractmethod
    def createTable(self) -> Table:
        pass


class ModermChair(Chair):
    def sit(self) -> str:
        return 'You are sitting on a moderm chair'


class ModermSofa(Sofa):
    def sit(self) -> str:
        return 'Your are sitting on a moderm sofa'


class ModermTable(Table):
    def serve(self) -> str:
        return 'You are serving on a moderm table'


class FournitureModermFactory(FournitureFactory):
    def createChair(self) -> ModermChair:
        return ModermChair()

    def createSofa(self) -> ModermSofa:
        return ModermSofa()

    def createTable(self) -> ModermTable:
        return ModermTable()


def client_code(factory: FournitureFactory):
    """
    El cliente entra a la tienda y sin importar que estilo es el que escoja se le deberá entregar el producto.
    Para este caso práctico, el cliente pedirá los trés productos.
    """
    return {
        'chair': factory.createChair(),
        'sofa': factory.createSofa(),
        'table': factory.createTable(),
    }


if __name__ == '__main__':
    products = client_code(FournitureModermFactory())

    print(products['chair'].sit())
    print(products['sofa'].sit())
    print(products['table'].serve())
