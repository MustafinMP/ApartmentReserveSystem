from abc import abstractmethod

from src.application.repositories import EmployeeRepository
from src.domain.employee.exceptions import EmployeeNotFound
from src.domain.employee.value_objects import EmployeeId


class DeleteEmployeeUseCase:
    @abstractmethod
    def execute(self, employee_id: EmployeeId) -> None:
        ...


class DeleteEmployeeUseCaseImpl(DeleteEmployeeUseCase):
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self, employee_id: EmployeeId) -> None:
        employee = self.employee_repository.find_by_id(employee_id)

        if employee is None:
            raise EmployeeNotFound

        self.employee_repository.delete(employee)


def new_delete_employee_usecase(employee_repository: EmployeeRepository) -> DeleteEmployeeUseCase:
    return DeleteEmployeeUseCaseImpl(employee_repository)
