from __future__ import annotations

from src.domain.employee.value_objects import EmployeeId, EmployeeFullname, EmployeePhoneNumber, EmployeeEmail
from src.domain.employee.value_objects.employee_password import EmployeePasswordHash


class Employee:
    def __init__(
            self,
            employee_id: EmployeeId,
            fullname: EmployeeFullname,
            phone_number: EmployeePhoneNumber,
            email: EmployeeEmail,
            password_hash: EmployeePasswordHash
    ):
        self._id = employee_id
        self._fullname = fullname
        self._phone_number = phone_number
        self._email = email
        self._password_hash = password_hash

    @property
    def id(self) -> EmployeeId:
        return self._id

    @property
    def fullname(self) -> EmployeeFullname:
        return self._fullname

    @property
    def phone_number(self) -> EmployeePhoneNumber:
        return self._phone_number

    @property
    def email(self) -> EmployeeEmail:
        return self._email

    @property
    def password_hash(self) -> EmployeePasswordHash:
        return self._password_hash

    def check_password_hash(self, password_hash: EmployeePasswordHash) -> bool:
        return self._password_hash.value == password_hash.value

    @staticmethod
    def create(
            fullname: EmployeeFullname,
            phone_number: EmployeePhoneNumber,
            email: EmployeeEmail,
            password_hash: EmployeePasswordHash
    ) -> Employee:
        return Employee(EmployeeId.generate(), fullname, phone_number, email, password_hash)
