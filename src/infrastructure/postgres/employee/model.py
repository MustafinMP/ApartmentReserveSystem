from __future__ import annotations

from uuid import UUID

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.employee.entities import Employee
from src.domain.employee.value_objects import EmployeeId, EmployeeFullname, EmployeePhoneNumber, EmployeeEmail
from src.domain.employee.value_objects.employee_password import EmployeePasswordHash
from src.infrastructure.postgres.database import Base


class EmployeeModel(Base):
    __tablename__ = 'employee'

    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=False)
    fullname: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)

    def to_entity(self) -> Employee:
        return Employee(
            employee_id=EmployeeId(self.id),
            fullname=EmployeeFullname(self.fullname),
            phone_number=EmployeePhoneNumber(self.phone_number),
            email=EmployeeEmail(self.email),
            password_hash=EmployeePasswordHash(self.password_hash)
        )

    @staticmethod
    def from_entity(employee: Employee) -> EmployeeModel:
        return EmployeeModel(
            id=employee.id.value,
            fullname=employee.fullname.value,
            phone_number=employee.phone_number.value,
            email=employee.email.value,
            password_hash=employee.password_hash.value
        )
