from Employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name, last_name)
        self._worked_hours = worked_hours
        self._rate = rate

    def get_salary(self):
        return self._worked_hours * self._rate
