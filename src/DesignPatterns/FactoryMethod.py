"""
FactoryMethod es un patrón de diseño creacional, dada una clase Creator con métodos que generan objetos de determinado
tipo (cómo se hace en la fábrica abstracta), permite heredar y modificar el tipo de objetos generados especializando su
funcionamiento.

Caso:
    Una empresa transportadora creó un sistema para automatizar el transporte de carga terrestre, el funcionamiento del
    misto, es que el cliente ingresa las características de la carta y el sistema solicita un camión y se lo asigna al
    cliente para su posterior carga. Esto fué un acierto por parte de la empresa, por lo cual empezaron a llegar
    solicitudes por parte del transporte marítimo.

    El problema es que este sistema solo fué pensado para camiones, por ende deben modificar el código para también te-
    ner en cuenta otros tipos de transporte.
"""
from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def download(self):
        pass


class Truck(Transport):
    def load(self):
        print("Payload loaded on the low bed")

    def download(self):
        print("Payload downloaded from the low bed")

    def __repr__(self):
        return f"Truck()"


class Ship(Transport):
    def load(self):
        print("Payload loaded on the deck")

    def download(self):
        print("Payload downloaded at the harbor")

    def __repr__(self):
        return f"Truck()"


class Creator(ABC):
    """
    Interfaz Creator, la cual provee el tipo pase y a partir de este se especializarán las clases
    """
    @abstractmethod
    def create_transport(self) -> Transport:
        """
        Este es el factory method, el cual generará un tipo determinado de transporte, pero aquí se definirá, pero no
        se especializará.
        """

    def get_transport(self) -> str:
        """
        Este método usará o llamará al factory methods y adicional antes de hacer este llamado pondrá determinada
        lógica.
        """
        transport = self.create_transport()
        return f"{self.__class__.__name__}, created {transport}"


class TruckCreator(Creator):
    def create_transport(self) -> Transport:
        return Truck()


class ShipCreator(Creator):
    def create_transport(self) -> Transport:
        return Ship()


def client_code():
    print("Client wants transport 2tons of haystacks")
    creator = TruckCreator()
    print(creator.get_transport())

    print("Client wants transport 20tons of merchandise from China to Perú")
    creator = ShipCreator()
    print(creator.get_transport())


if __name__ == '__main__':
    client_code()
