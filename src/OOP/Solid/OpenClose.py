from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return f'Person(name={self._name})'


class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass


class PersonDb(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to database')


class PersonJson(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a JSON file')


class PersonXml(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a XML file')


if __name__ == '__main__':
    inst = Person('Kevin Daniel Guzman Delgadillo')

    storage = PersonXml()
    storage.save(inst)
