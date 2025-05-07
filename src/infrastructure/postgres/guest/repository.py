from typing import Optional

from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from src.application.repositories.guest_repository import GuestRepository
from src.domain.guest.entities import Guest
from src.domain.guest.value_objects import GuestId, GuestPhoneNumber
from src.infrastructure.postgres.guest.model import GuestModel


class GuestRepositoryImpl(GuestRepository):
    """SQLite implementation of Guest repository interface."""

    def __init__(self, session: Session):
        """Initialize repository with SQLAlchemy session."""
        self.session = session

    def save(self, guest: Guest):
        """Save a Guest"""

        guest_model = GuestModel.from_entity(guest)

        stmt = select(GuestModel).where(GuestModel.id == guest.id.value)
        existing_guest = self.session.scalar(stmt)

        if existing_guest is None:
            self.session.add(guest_model)
        else:
            existing_guest.fullname = guest_model.fullname
            existing_guest.phone_number = guest_model.phone_number
            self.session.merge(existing_guest)

    def find_by_id(self, guest_id: GuestId) -> Optional[Guest]:
        """Find a Guest by ID"""

        stmt = select(GuestModel).where(GuestModel.id == guest_id.value)
        guest = self.session.scalar(stmt)

        return guest.to_entity() if guest is not None else None

    def find_by_phone_number(self, guest_phone_number: GuestPhoneNumber) -> Optional[Guest]:
        """Find a Guest by Phone Number"""

        stmt = select(GuestModel).where(GuestModel.phone_number == guest_phone_number.value)
        guest = self.session.scalar(stmt)

        return guest.to_entity() if guest is not None else None

    def find_all(self) -> list[Guest]:
        """Get all Guests"""

        stmt = select(GuestModel)
        return [
            guest.to_entity()
            for guest in self.session.scalars(stmt)
        ]

    def delete(self, guest_id: GuestId) -> None:
        """Delete a Guest by ID"""

        stmt = delete(GuestModel).where(GuestModel.id == guest_id.value)
        self.session.execute(stmt)


def new_guest_repository(session: Session) -> GuestRepository:
    """Create a new GuestRepository instance."""
    return GuestRepositoryImpl(session)
