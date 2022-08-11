# Los métodos estáticos en Python, no están vinculados con la clase o sus instancias, por lo cual se utilizan en las
# clases cómo agrupaciones de pequeños métodos.
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return 9 * celsius / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return 5 * (fahrenheit - 32) / 9


print(TemperatureConverter.celsius_to_fahrenheit(30))
