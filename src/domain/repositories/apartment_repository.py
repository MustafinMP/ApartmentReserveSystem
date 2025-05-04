from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities import Apartment
from src.domain.entity_values.apartment import ApartmentId


class ApartmentRepository(ABC):
    @abstractmethod
    def save(self, apartment: Apartment):
        """Save an Apartment"""

    @abstractmethod
    def find_by_id(self, apartment_id: ApartmentId) -> Optional[Apartment]:
        """Find an Apartment by ID"""

    @abstractmethod
    def find_all(self) -> list[Apartment]:
        """Get all Apartments"""

    @abstractmethod
    def delete(self, apartment_id: ApartmentId) -> None:
        """Delete an Apartment by ID"""