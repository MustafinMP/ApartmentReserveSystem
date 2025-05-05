from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class ApartmentDescription:
    value: str

    def __str__(self):
        return self.value