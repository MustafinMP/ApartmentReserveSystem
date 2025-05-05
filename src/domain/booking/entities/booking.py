from __future__ import annotations

from src.domain.apartment.entities import Apartment
from src.domain.booking.value_objects import BookingPeriod, BookingId
from src.domain.guest.entities import Guest


class Booking:
    def __init__(self, booking_id: BookingId, guest: Guest, apartment: Apartment, date: BookingPeriod):
        self._id = booking_id
        self._guest = guest
        self._apartment = apartment
        self._date = date
        self._is_paid_for = False

    def overlaps(self, other: Booking) -> bool:
        return self._apartment == other._apartment and self._date.overlaps(other._date)

    def total_amount(self) -> float:
        return self._apartment.rent_amount.value * self._date.days()

    def is_paid_for(self) -> bool:
        return self._is_paid_for

    @staticmethod
    def create(guest: Guest, apartment: Apartment, date: BookingPeriod) -> Booking:
        return Booking(BookingId.generate(), guest, apartment, date)
