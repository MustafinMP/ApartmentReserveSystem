from abc import abstractmethod

from src.application.repositories import ApartmentRepository
from src.domain.apartment.entities import Apartment
from src.domain.apartment.value_objects import ApartmentId


class FindApartmentBuIdUseCase:
    @abstractmethod
    def execute(self, apartment_id: ApartmentId) -> Apartment:
        ...


class FindApartmentBuIdUseCaseImpl(FindApartmentBuIdUseCase):
    def __init__(self, apartment_repository: ApartmentRepository):
        self.apartment_repository = apartment_repository

    def execute(self, apartment_id: ApartmentId) -> Apartment:
        apartment = self.apartment_repository.find_by_id(apartment_id)
        return apartment


def new_find_apartment_by_id_usecase(apartment_repository: ApartmentRepository) -> FindApartmentBuIdUseCase:
    return FindApartmentBuIdUseCaseImpl(apartment_repository)