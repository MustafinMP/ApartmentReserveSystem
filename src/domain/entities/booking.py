from __future__ import annotations
from src.domain.entities import Guest, Apartment
from src.domain.entity_values.booking import BookingPeriod, BookingId


class Booking:
    def __init__(self, booking_id: BookingId, guest: Guest, apartment: Apartment, date: BookingPeriod):
        self._id = booking_id
        self._guest = guest
        self._apartment = apartment
        self._date = date

    def overlaps(self, other: Booking) -> bool:
        return self._apartment == other._apartment and self._date.overlaps(other._date)

    def total_cost(self) -> float:
        return self._apartment.cost.value * self._date.days()

    @staticmethod
    def create(guest: Guest, apartment: Apartment, date: BookingPeriod) -> Booking:
        return Booking(BookingId.generate(), guest, apartment, date)
