from abc import ABC, abstractmethod
from vehicles import Vehicle, Motorcycle, Car


class Builder(ABC):
    def __init__(self):
        self._vehicle = None

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def getVehicle(self) -> Vehicle:
        pass

    def setInsurance(self, value: bool):
        self._vehicle.insurance = value

    def setTripAssistance(self, value: bool):
        self._vehicle.trip_assistance = value

    def setGps(self, value: bool):
        self._vehicle.gps = value

    def setMaxSpeed(self, value: float):
        self._vehicle.max_speed = value

    def setTorque(self, value: float):
        self._vehicle.torque = value

    def setMotorSize(self, value: float):
        self._vehicle.motor_size = value


class MotorcycleBuilder(Builder):
    def reset(self):
        self._vehicle = Motorcycle()

    def getVehicle(self) -> Motorcycle:
        return self._vehicle

    def setCylinders(self, value: int):
        self._vehicle.cylinders = value


class CarBuilder(Builder):
    def reset(self):
        self._vehicle = Car()

    def setPayload(self, value: float):
        self._vehicle.payload = value

    def setType(self, value: str):
        self._vehicle.type = value

    def getVehicle(self) -> Car:
        return self._vehicle
