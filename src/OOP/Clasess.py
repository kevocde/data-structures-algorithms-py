# Atributos de clase
class Human:
    counter = 0

    def __init__(self, age, gender):
        Human.counter += 1

        self.age = age
        self.gender = gender

    def greet(self):
        return f"Hi, it's a {self.gender} of {self.age} years old."


# Se pueden acceder al atributo de clase desde la misma clase o desde las clases hijas, pero siempre la posición,
# en memoria será la misma.
human1 = Human(21, 'male')
human2 = Human(23, 'female')

print(Human.counter)
print(human1.counter)
print(human2.counter)

