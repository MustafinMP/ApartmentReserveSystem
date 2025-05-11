from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel

from src.domain.guest.entities import Guest


class GuestSchema(BaseModel):
    id: UUID
    fullname: str
    phone_number: str

    @staticmethod
    def from_entity(entity: Guest) -> GuestSchema:
        return GuestSchema(
            id=entity.id.value,
            fullname=entity.fullname.value,
            phone_number=entity.phone_number.value
        )


class CreateGuestSchema(BaseModel):
    fullname: str
    phone_number: str
