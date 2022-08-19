from Employee import Employee


class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self._salary = salary

    def get_salary(self):
        return self._salary
