"""
El patrón de diseño Singleton es uno de los más utilizados en la actualidad; su funcionalidad es que sin importar cómo
sea llamado o cuantas veces sea llamado determinado objeto, su instancia siempre será la misma en todas partes,
esto es especialmente útil para centralizar determinadas operaciones y añadir niveles de acceso a las mismas.
"""


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        El método mágico __call__ es llamado cuando se invoca determinada clase cón si fuese un función, por ejemplo
        cuando se quiere generar una instancia de esa clase. Se interfiere el funcionamiento de esta para que por medio
        de una variable de clase sea almacenada la primera instancia y luego siempre al tratar de crear un objeto nuevo
        siempre se devolverá la misma.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class DBAccess(metaclass=SingletonMeta):
    HOST = 'localhost'

    def __init__(self, name: str, user: str, password: str = '', host: str = HOST):
        self._name = name
        self._user = user
        self._password = password
        self._host = host

    def persons(self):
        return []


if __name__ == '__main__':
    db = DBAccess('test', 'root')
    db2 = DBAccess('test', 'root')

    if id(db) == id(db2):
        print('The singleton pattern works')
