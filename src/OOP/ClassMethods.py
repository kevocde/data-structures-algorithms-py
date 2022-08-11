# Los métodos de clase al igual que las propiedades de clase, son compartidos entre todas las intancias,
# pero estos reciben un parámetro en lugar de ser la instancia propia, será la clase.
class Human:
    counter = 0

    def __init__(self, full_name, gender, age):
        Human.counter += 1

        self.full_name = full_name
        self.gender = gender
        self.age = age

    def greet(self):
        return f"Hi there, I'm {self.full_name}, and I'm a specimen {self.gender} of {self.age} years old."

    @classmethod
    def create_male(cls, full_name, age):
        return Human(full_name, 'male', age)


human1 = Human.create_male('Kevin Guzman', 24)
print(human1.greet())
