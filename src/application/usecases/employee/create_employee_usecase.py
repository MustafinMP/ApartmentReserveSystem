from abc import abstractmethod

from src.application.repositories import EmployeeRepository
from src.domain.employee.entities import Employee
from src.domain.employee.value_objects import EmployeeFullname, EmployeePhoneNumber, EmployeeEmail
from src.domain.employee.value_objects.employee_password import EmployeePassword


class CreateEmployeeUseCase:
    @abstractmethod
    def execute(
            self,
            fullname: EmployeeFullname,
            phone_number: EmployeePhoneNumber,
            email: EmployeeEmail,
            password: EmployeePassword
    ) -> Employee:
        ...


class CreateEmployeeUseCaseImpl(CreateEmployeeUseCase):
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(
            self,
            fullname: EmployeeFullname,
            phone_number: EmployeePhoneNumber,
            email: EmployeeEmail,
            password: EmployeePassword
    ) -> Employee:
        employee = Employee.create(fullname, phone_number, email, password.to_hash())
        self.employee_repository.save(employee)
        return employee


def new_create_employee_usecase(employee_repository: EmployeeRepository) -> CreateEmployeeUseCase:
    return CreateEmployeeUseCaseImpl(employee_repository)
