# Las clases pueden utilizarse, cómo padres o hijas de otras clases con la finalidad de especializar y reeutilizar
# código.
class Human:
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age

    def greet(self):
        return f"I'm a speciment {self.gender} of {self.age} years old"


# This class inherit from Human
class Person(Human):
    def __init__(self, full_name, gender, age):
        super().__init__(gender, age)
        self.full_name = full_name

    def greet(self):
        """Aquí se está sobreescribiendo el método"""
        return f"Hi, I'm {self.full_name}, " + super().greet()


# Se crea la instancia de Person
person1 = Person('Kevin Arboleda', 'male', 24)
print(person1.greet())
