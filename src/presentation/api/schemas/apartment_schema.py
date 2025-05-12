from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel

from src.domain.apartment.entities import Apartment
from src.domain.apartment.value_objects import ApartmentId, ApartmentName, ApartmentDescription, ApartmentAddress, \
    ApartmentRent


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

    def to_entity(self) -> Apartment:
        return Apartment(
            ApartmentId(self.id),
            ApartmentName(self.name),
            ApartmentDescription(self.description),
            ApartmentAddress(self.address),
            ApartmentRent(self.rent)
        )



class CreateApartmentSchema(BaseModel):
    name: str
    description: str
    address: str
    rent: float
