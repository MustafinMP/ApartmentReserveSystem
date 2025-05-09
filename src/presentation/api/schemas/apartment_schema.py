from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel

from src.domain.apartment.entities import Apartment


class ApartmentSchema(BaseModel):
    id: UUID
    name: str
    description: str
    address: str
    rent: float

    @staticmethod
    def from_entity(entity: Apartment) -> ApartmentSchema:
        return ApartmentSchema(
            id=entity.id.value,
            name=entity.name.value,
            description=entity.description.value,
            address=entity.address.value,
            rent=entity.rent.value
        )


class CreateApartmentSchema(BaseModel):
    name: str
    description: str
    address: str
    rent: float
