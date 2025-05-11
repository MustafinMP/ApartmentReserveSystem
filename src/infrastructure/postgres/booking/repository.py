from typing import Optional

from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from src.application.repositories import BookingRepository
from src.domain.apartment.entities import Apartment
from src.domain.apartment.value_objects import ApartmentId
from src.domain.booking.entities import Booking
from src.domain.booking.value_objects import BookingId
from src.domain.guest.entities import Guest
from src.domain.guest.value_objects import GuestId
from src.infrastructure.postgres.apartment.model import ApartmentModel
from src.infrastructure.postgres.booking.model import BookingModel
from src.infrastructure.postgres.guest.model import GuestModel


class BookingRepositoryImpl(BookingRepository):
    """SQLite implementation of Booking repository interface."""

    def __init__(self, session: Session):
        """Initialize repository with SQLAlchemy session."""
        self.session = session

    def save(self, booking: Booking):
        """Save a Booking"""

        booking_model = BookingModel.from_entity(booking)

        stmt = select(BookingModel).where(BookingModel.id == booking.id.value)
        existing_booking: BookingModel = self.session.scalar(stmt)

        if existing_booking is None:
            self.session.add(booking_model)
        else:
            existing_booking.date_from = booking_model.date_from
            existing_booking.date_to = booking_model.date_to
            existing_booking.apartment_id = booking_model.apartment_id
            existing_booking.guest_id = booking_model.guest_id
            existing_booking.is_paid_for = booking_model.is_paid_for
            existing_booking.is_finished = booking_model.is_finished
            self.session.merge(existing_booking)

    def find_by_id(self, booking_id: BookingId) -> Optional[Booking]:
        """Find a Booking by ID"""

        stmt = select(BookingModel).where(BookingModel.id == booking_id.value)
        booking = self.session.scalar(stmt)

        # хорошо бы сделать защиту от удаленных пользователей и квартир, но не сейчас
        return booking.to_entity(
            self._find_apartment_by_id(ApartmentId(booking.apartment_id)),
            self._find_guest_by_id(GuestId(booking.guest_id))
        ) if booking is not None else None

    def _find_apartment_by_id(self, apartment_id: ApartmentId) -> Optional[Apartment]:
        """Find an Apartment by ID"""

        stmt = select(ApartmentModel).where(ApartmentModel.id == apartment_id.value)
        apartment = self.session.scalar(stmt)

        return apartment.to_entity() if apartment is not None else None

    def _find_guest_by_id(self, guest_id: GuestId) -> Optional[Guest]:
        """Find a Guest by ID"""

        stmt = select(GuestModel).where(GuestModel.id == guest_id.value)
        guest = self.session.scalar(stmt)

        return guest.to_entity() if guest is not None else None

    def find_by_guest(self, guest: Guest) -> list[Booking]:
        """Find a Booking by Guest"""

        stmt = select(BookingModel).where(BookingModel.guest_id == guest.id.value)
        return [
            booking.to_entity(
                self._find_apartment_by_id(ApartmentId(booking.apartment_id)),
                guest
            )
            for booking in self.session.scalars(stmt)
        ]

    def find_by_apartment(self, apartment: Apartment) -> list[Booking]:
        """Find a Booking by Apartment"""

        stmt = select(BookingModel).where(BookingModel.apartment_id == apartment.id.value)
        return [
            booking.to_entity(
                apartment,
                self._find_guest_by_id(GuestId(booking.guest_id))
            )
            for booking in self.session.scalars(stmt)
        ]

    def find_all(self) -> list[Booking]:
        """Get all Bookings"""

        stmt = select(BookingModel)
        return [
            booking.to_entity(
                self._find_apartment_by_id(ApartmentId(booking.apartment_id)),
                self._find_guest_by_id(GuestId(booking.guest_id))
            )
            for booking in self.session.scalars(stmt)
        ]

    def delete(self, booking_id: BookingId) -> None:
        """Delete a Booking by ID"""

        stmt = delete(BookingModel).where(BookingModel.id == booking_id.value)
        self.session.execute(stmt)


def new_booking_repository(session: Session) -> BookingRepository:
    """Create a new BookingRepository instance."""
    return BookingRepositoryImpl(session)
