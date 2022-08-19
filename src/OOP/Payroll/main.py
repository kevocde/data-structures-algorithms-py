from faker import Faker
from Payroll import Payroll
from FulltimeEmployee import FulltimeEmployee
from HourlyEmployee import HourlyEmployee


def fulltime_employee_maker(payroll_inst, count):
    Faker.seed(0)
    faker = Faker()

    for _ in range(count):
        employee = FulltimeEmployee(faker.first_name(), faker.last_name(), faker.random_number(6))
        payroll_inst.add(employee)


def hourly_employee_maker(payroll_inst, count):
    Faker.seed(0)
    faker = Faker()

    for _ in range(count):
        employee = HourlyEmployee(faker.first_name(), faker.last_name(), faker.random_int(10, 480), 20)
        payroll_inst.add(employee)


if __name__ == '__main__':
    payroll = Payroll()

    fulltime_employee_maker(payroll, 150)
    hourly_employee_maker(payroll, 200)
    payroll.print()
