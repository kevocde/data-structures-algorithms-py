class Payroll:
    def __init__(self):
        self._employee_list = []

    def add(self, employee):
        self._employee_list.append(employee)

    def print(self):
        for idx, employee in enumerate(self._employee_list):
            print("{}. {}: $ {:0,.2f}".format((idx + 1), employee.full_name, employee.get_salary()))
