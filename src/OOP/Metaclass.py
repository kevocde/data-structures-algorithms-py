from pprint import pprint


class Prop:
    def __init__(self, attr):
        self._attr = attr

    def get(self, class_):
        return getattr(class_, self._attr)

    def set(self, class_, value):
        return setattr(class_, self._attr, value)

    def delete(self, class_):
        return delattr(class_, self._attr)


class Autofill(type):
    def __new__(mcs, name, bases, class_dict, **kwargs):
        class_ = super().__new__(mcs, name, bases, class_dict)

        Autofill.createObjectVariables(class_, kwargs)
        Autofill.createInstanceVariables(class_)
        Autofill.defineAutomaticInitialization(class_)

        return class_

    @staticmethod
    def createObjectVariables(class_, kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if not hasattr(class_, key):
                    setattr(class_, key, value)

    @staticmethod
    def createInstanceVariables(class_):
        if hasattr(class_, 'props'):
            for prop in class_.props:
                attr = f'_{prop}'
                prop_ins = property(
                    fget=Prop(attr).get,
                    fset=Prop(attr).set,
                    fdel=Prop(attr).delete,
                )
                setattr(class_, prop, prop_ins)

    @staticmethod
    def defineAutomaticInitialization(class_):
        def _init(self, *args, **kwargs):
            if kwargs:
                for arg in class_.props:
                    if arg in kwargs.keys():
                        setattr(self, arg, kwargs[arg])

            if args:
                for arg in zip(class_.props, args):
                    setattr(self, arg[0], arg[1])

        setattr(class_, '__init__', _init)


class Person(metaclass=Autofill, freedom=True, country='USA'):
    props = ['name', 'age']


if __name__ == '__main__':
    print('First adds to Person class the object variables')
    pprint(Person.__dict__)

    print('Later adds to Person\'s instance the properties')
    person = Person('Kevin Guzman', age=24)
    pprint(person.__dict__)
