from __future__ import annotations

from datetime import date
from uuid import UUID

from sqlalchemy import String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.apartment.entities import Apartment
from src.domain.booking.entities import Booking
from src.domain.booking.value_objects import BookingId, BookingDates
from src.domain.guest.entities import Guest
from src.infrastructure.postgres.database import Base



class BookingModel(Base):
    __tablename__ = 'booking'

    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=False)
    date_from: Mapped[date] = mapped_column(Date, nullable=False)
    date_to: Mapped[date] = mapped_column(Date, nullable=False)
    is_paid_for: Mapped[bool] = mapped_column(Boolean, nullable=False)
    is_finished: Mapped[bool] = mapped_column(Boolean, nullable=False)
    guest_id: Mapped[UUID] = mapped_column(ForeignKey('guest.id'), nullable=False)
    apartment_id: Mapped[UUID] = mapped_column(ForeignKey('apartment.id'), nullable=False)

    def to_entity(self, guest: Guest, apartment: Apartment) -> Booking:
        return Booking(
            booking_id=BookingId(self.id),
            guest=guest,
            apartment=apartment,
            date=BookingDates(self.date_from, self.date_to),
            paid_for=self.is_paid_form,
            finished=self.is_finished
        )

    @staticmethod
    def from_entity(booking: Booking) -> BookingModel:
        return BookingModel(
            id=booking.id.value,
            date_from=booking.dates.date_from,
            date_to=booking.dates.date_to,
            is_paid_for=booking.is_paid_for,
            is_finished=booking.finished,
            guest_id=booking.guest.id.value,
            apartment_id=booking.apartment.id.value
        )
