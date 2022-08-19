from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @abstractmethod
    def get_salary(self):
        pass
