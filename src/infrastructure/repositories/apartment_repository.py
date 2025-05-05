from typing import Optional

from src.domain.apartment.entities.apartment import Apartment
from src.domain.apartment.value_objects import ApartmentId
from src.application.repositories import ApartmentRepository


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
