"""
Este es el mismo patron singleton pero al trabajar con dos hilos en paralelo, es necesario realizar un bloque de la
creación para que por hilo no se duplique la instancia creada.
"""
from threading import Lock, Thread


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == '__main__':
    process = Thread(target=test_singleton, args=("Foo",))
    process1 = Thread(target=test_singleton, args=("Bar",))

    process.start()
    process1.start()
