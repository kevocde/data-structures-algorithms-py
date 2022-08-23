"""
Builder es un patrón de diseño creacional. Este patrón de diseño se usa cuando se posee un proceso demasiado extenso
para la creación de un grupo de objetos del mismo tipo (heredados).

La siguiente ejemplo implementa este patrón:
    En el concesionario de Autogermana se venden motos y automóbiles de alta gama, cada uno con servicios en común.
    En el segmento de motos las características son la cilindrada de la moto, el número de cilindros, el torque y
    la velocidad máxima alcanzada; para el segmento de autos, las características son el tamaño del motor, la capacidad
    de carga, el torque y el tipo, camioneta, familiar y deportivo. Ambos tipos de vehículos poseen precio y servicios
    adicioneles cómo gps, asistencia en carretera y seguro todo riesgo.
"""
from vehicles import Motorcycle
from builders import MotorcycleBuilder, CarBuilder


class Director:
    SPORT_MOTORCYCLE = {
        'insurance': False,
        'tripAssistance': False,
        'gps': True,
        'maxSpeed': 247.0,
        'torque': 56.0,
        'motorSize': 549.5,
        'cylinders': 2
    }

    @classmethod
    def makeSportMotorcycle(cls) -> Motorcycle:
        builder = MotorcycleBuilder()
        builder.reset()

        for key, value in cls.SPORT_MOTORCYCLE.items():
            getattr(builder, f'set{key[:1].upper()}{key[1:]}')(value)

        return builder.getVehicle()


if __name__ == '__main__':
    print("The client wants a Sport Motorcycle:")
    print(Director.makeSportMotorcycle())
