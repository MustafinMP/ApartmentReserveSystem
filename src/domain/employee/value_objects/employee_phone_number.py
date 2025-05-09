from dataclasses import dataclass


@dataclass(frozen=True)
class EmployeePhoneNumber:
    value: str

