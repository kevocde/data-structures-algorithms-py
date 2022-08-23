from abc import ABC


class Vehicle(ABC):
    def __init__(self):
        self.insurance = False
        self.trip_assistance = False
        self.gps = True
        self.max_speed = None
        self.torque = None
        self.motor_size = None

    @property
    def motor_size(self) -> float:
        return self._motor_size

    @motor_size.setter
    def motor_size(self, value: float):
        self._motor_size = value

    @property
    def torque(self) -> float:
        return self._torque

    @torque.setter
    def torque(self, value: float):
        self._torque = value

    @property
    def max_speed(self) -> float:
        return self._max_speed

    @max_speed.setter
    def max_speed(self, value: float):
        self._max_speed = value

    @property
    def gps(self) -> bool:
        return self._gps

    @gps.setter
    def gps(self, value: bool):
        self._gps = value

    @property
    def trip_assistance(self) -> bool:
        return self._trip_assistance

    @trip_assistance.setter
    def trip_assistance(self, value: bool):
        self._trip_assistance = value

    @property
    def insurance(self) -> bool:
        return self._insurance

    @insurance.setter
    def insurance(self, value: bool):
        self._insurance = value

    def accelerate(self) -> callable:
        return lambda x: (self._max_speed / x)


class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__()
        self.cylinders = None

    @property
    def cylinders(self) -> int:
        return self._cylinders

    @cylinders.setter
    def cylinders(self, value: int):
        self._cylinders = value

    def __repr__(self) -> str:
        return f'Motorcycle(insurance={self.insurance}, trip_assistance={self.trip_assistance}, gps={self.gps}, ' \
               f'max_speed={self.max_speed}, torque={self.torque}, motor_size={self.motor_size}, ' \
               f'cylinders={self.cylinders})'


class Car(Vehicle):
    TRUCK = 'truck'
    FAMILIAR = 'family'
    SPORT = 'sport'

    def __init__(self):
        super().__init__()
        self.payload = None
        self.type = self.FAMILIAR

    @property
    def payload(self) -> int:
        return self._payload

    @payload.setter
    def payload(self, value: int):
        self._payload = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        if value not in (self.TRUCK, self.FAMILIAR, self.SPORT):
            raise ValueError('Invalid type of car')

        self._type = value
