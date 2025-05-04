from typing import Optional

from src.domain.entities.apartment import Apartment
from src.domain.entity_values.apartment import ApartmentId
from src.domain.repositories.apartment_repository import ApartmentRepository


class ApartmentRepositoryImpl(ApartmentRepository):

    def __init__(self, session):
        ...

    def save(self, apartment: Apartment):
        ...

    def find_by_id(self, apartment_id: ApartmentId) -> Optional[Apartment]:
        ...

    def find_all(self) -> list[Apartment]:
        ...

    def delete(self, apartment_id: ApartmentId) -> None:
        ...
