from abc import ABC, abstractmethod
from typing import Optional

from src.domain.guest.entities import Guest
from src.domain.guest.value_objects import GuestId, GuestPhoneNumber


class GuestRepository(ABC):
    @abstractmethod
    def save(self, guest: Guest):
        """Save a Guest"""

    @abstractmethod
    def find_by_id(self, guest_id: GuestId) -> Optional[Guest]:
        """Find a Guest by ID"""

    @abstractmethod
    def find_by_phone_number(self, guest_phone_number: GuestPhoneNumber) -> Optional[Guest]:
        """Find a Guest by Phone Number"""

    @abstractmethod
    def find_all(self) -> list[Guest]:
        """Get all Guests"""

    @abstractmethod
    def delete(self, guest_id: GuestId) -> None:
        """Delete a Guest by ID"""
