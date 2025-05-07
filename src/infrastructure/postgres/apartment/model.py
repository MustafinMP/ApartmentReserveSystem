from __future__ import annotations

from uuid import UUID

from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.apartment.entities import Apartment
from src.domain.apartment.value_objects import ApartmentId, ApartmentName, ApartmentDescription, ApartmentAddress, \
    ApartmentRent
from src.infrastructure.postgres.database import Base



class ApartmentModel(Base):
    __tablename__ = 'apartment'

    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    rent: Mapped[float] = mapped_column(Float, nullable=False)

    def to_entity(self) -> Apartment:
        return Apartment(
            apartment_id=ApartmentId(self.id),
            name=ApartmentName(self.name),
            description=ApartmentDescription(self.description),
            address=ApartmentAddress(self.address),
            rent=ApartmentRent(self.rent)
        )

    @staticmethod
    def from_entity(apartment: Apartment) -> ApartmentModel:
        return ApartmentModel(
            apartment_id=apartment.id.value,
            name=apartment.name.value,
            description=apartment.description.value,
            address=apartment.address.value,
            rent=apartment.rent.value
        )
