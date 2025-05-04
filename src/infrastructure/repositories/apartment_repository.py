from src.domain.entities.apartment import Apartment
from src.domain.repositories.apartment_repository import ApartmentRepository


class ApartmentRepositoryImpl(ApartmentRepository):
    def __init__(self, session):
        ...

    def save(self, apartment: Apartment):
        ...