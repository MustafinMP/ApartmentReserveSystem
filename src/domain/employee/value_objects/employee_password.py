from dataclasses import dataclass
from hashlib import sha256


@dataclass(frozen=True)
class EmployeePassword:
    value: str

    def __post_init__(self):
        ...

    def to_hash(self):
        return EmployeePasswordHash(str(sha256(self.value)))


@dataclass(frozen=True)
class EmployeePasswordHash:
    value: str
