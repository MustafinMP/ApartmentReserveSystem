from __future__ import annotations
from dataclasses import dataclass
from datetime import date

from src.domain.booking.exceptions import InvalidBookingDate


@dataclass(frozen=True)
class BookingPeriod:
    date_from: date
    date_to: date

    def __post_init__(self):
        if self.date_from >= self.date_to:  # можно вынести в одно поле
            raise InvalidBookingDate

    def overlaps(self, other: BookingPeriod) -> bool:
        return self.date_from <= other.date_from < self.date_to or other.date_from <= self.date_from < other.date_to

    def days(self) -> int:
        return (self.date_to - self.date_from).days
