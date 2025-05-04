from __future__ import annotations
from dataclasses import dataclass
from uuid import uuid4, UUID


@dataclass(frozen=True)
class BookingId:
    value: UUID

    @classmethod
    def generate(cls):
        return cls(value=uuid4())
