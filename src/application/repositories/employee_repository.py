from abc import ABC, abstractmethod
from typing import Optional

from src.domain.employee.entities import Employee
from src.domain.employee.value_objects import EmployeeId, EmployeePhoneNumber


class EmployeeRepository(ABC):
    @abstractmethod
    def save(self, employee: Employee):
        """Save an Employee"""

    @abstractmethod
    def find_by_id(self, employee_id: EmployeeId) -> Optional[Employee]:
        """Find an Employee by ID"""

    @abstractmethod
    def find_by_phone_number(self, employee_phone_number: EmployeePhoneNumber) -> Optional[Employee]:
        """Find an Employee by Phone Number"""

    @abstractmethod
    def find_all(self) -> list[Employee]:
        """Get all Employees"""

    @abstractmethod
    def delete(self, employee_id: EmployeeId) -> None:
        """Delete an Employee by ID"""
