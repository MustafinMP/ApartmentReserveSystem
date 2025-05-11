from __future__ import annotations

from src.domain.apartment.entities import Apartment
from src.domain.booking.exceptions import BookingIsNotPayed
from src.domain.booking.value_objects import BookingDates, BookingId
from src.domain.guest.entities import Guest


class Booking:
    def __init__(
            self,
            booking_id: BookingId,
            guest: Guest,
            apartment: Apartment,
            date: BookingDates,
            paid_for: bool = False,
    finished: bool = False
    ):
        self._id = booking_id
        self._guest = guest
        self._apartment = apartment
        self._date = date
        self._is_paid_for = paid_for
        self._finished = finished

    def overlaps(self, other: Booking) -> bool:
        return self._apartment == other._apartment and self._date.overlaps(other._date)

    def total_amount(self) -> float:
        return self._apartment.rent_amount.value * self._date.days()

    @property
    def id(self) -> BookingId:
        return self._id

    @property
    def apartment(self) -> Apartment:
        return self._apartment

    @property
    def guest(self) -> Guest:
        return self._guest

    @property
    def dates(self) -> BookingDates:
        return self._date

    @property
    def is_paid_for(self) -> bool:
        return self._is_paid_for

    @property
    def finished(self) -> bool:
        return self._finished

    def pay(self) -> None:
        self._is_paid_for = True

    def finish(self) -> None:
        if not self._is_paid_for:
            raise BookingIsNotPayed
        self._finished = True

    @staticmethod
    def create(guest: Guest, apartment: Apartment, date: BookingDates) -> Booking:
        return Booking(BookingId.generate(), guest, apartment, date)
