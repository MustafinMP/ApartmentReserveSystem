from typing import Optional

from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from src.application.repositories import ApartmentRepository
from src.domain.apartment.entities import Apartment
from src.domain.apartment.value_objects import ApartmentId
from src.infrastructure.postgres.apartment.model import ApartmentModel


class ApartmentRepositoryImpl(ApartmentRepository):
    """SQLite implementation of Apartment repository interface."""

    def __init__(self, session: Session):
        """Initialize repository with SQLAlchemy session."""
        self.session = session

    def save(self, apartment: Apartment):
        """Save an Apartment"""

        apartment_model = ApartmentModel.from_entity(apartment)

        stmt = select(ApartmentModel).where(ApartmentModel.id == apartment.id.value)
        existing_apartment = self.session.scalar(stmt)

        if existing_apartment is None:
            self.session.add(apartment_model)
        else:
            existing_apartment.name = apartment_model.name
            existing_apartment.description = apartment_model.description
            existing_apartment.address = apartment_model.address
            existing_apartment.rent = apartment_model.rent
            self.session.merge(existing_apartment)

    def find_by_id(self, apartment_id: ApartmentId) -> Optional[Apartment]:
        """Find an Apartment by ID"""

        stmt = select(ApartmentModel).where(ApartmentModel.id == apartment_id.value)
        apartment = self.session.scalar(stmt)

        return apartment.to_entity() if apartment is not None else None

    def find_all(self) -> list[Apartment]:
        """Get all Apartments"""

        stmt = select(ApartmentModel)
        return [
            apartment.to_entity()
            for apartment in self.session.scalars(stmt)
        ]

    def delete(self, apartment_id: ApartmentId) -> None:
        """Delete an Apartment by ID"""

        stmt = delete(ApartmentModel).where(ApartmentModel.id == apartment_id.value)
        self.session.execute(stmt)


def new_apartment_repository(session: Session) -> ApartmentRepository:
    """Create a new ApartmentRepository instance."""
    return ApartmentRepositoryImpl(session)
