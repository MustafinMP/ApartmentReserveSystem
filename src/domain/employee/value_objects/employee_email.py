from dataclasses import dataclass


@dataclass(frozen=True)
class EmployeeEmail:
    value: str
