from __future__ import annotations

from datetime import date
from uuid import UUID

from pydantic import BaseModel

from src.domain.booking.entities import Booking
from src.presentation.api.schemas import ApartmentSchema
from src.presentation.api.schemas.guest_schema import GuestSchema


class BookingSchema(BaseModel):
    id: UUID
    apartment: ApartmentSchema
    guest: GuestSchema
    date_from: date
    date_to: date

    @staticmethod
    def from_entity(entity: Booking) -> BookingSchema:
        return BookingSchema(
            id=entity.id.value,
            apartment=ApartmentSchema.from_entity(entity.apartment),
            guest=GuestSchema.from_entity(entity.guest),
            date_from=entity.dates.date_from,
            date_to=entity.dates.date_to
        )


class CreateBookingSchema(BaseModel):
    id: UUID
    apartment: ApartmentSchema
    guest: GuestSchema
    date_from: date
    date_to: date
