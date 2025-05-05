from abc import ABC, abstractmethod
from typing import Optional

from src.domain.apartment.entities import Apartment
from src.domain.booking.entities import Booking
from src.domain.booking.value_objects import BookingId
from src.domain.guest.entities import Guest


class BookingRepository(ABC):
    @abstractmethod
    def save(self, booking: Booking):
        """Save a Booking"""

    @abstractmethod
    def find_by_id(self, booking_id: BookingId) -> Optional[Booking]:
        """Find a Booking by ID"""

    @abstractmethod
    def find_by_guest(self, guest: Guest) -> list[Booking]:
        """Find a Booking by Guest"""

    @abstractmethod
    def find_by_apartment(self, apartment: Apartment) -> list[Booking]:
        """Find a Booking by Apartment"""

    @abstractmethod
    def find_all(self) -> list[Booking]:
        """Get all Bookings"""

    @abstractmethod
    def delete(self, booking_id: BookingId) -> None:
        """Delete a Booking by ID"""
