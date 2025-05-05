from abc import abstractmethod

from src.domain.apartment.entities import Apartment
from src.domain.apartment.value_objects import ApartmentName, ApartmentDescription, ApartmentRent
from src.domain.apartment.value_objects.apartment_address import ApartmentAddress
from src.application.repositories import ApartmentRepository


class CreateApartmentUseCase:
    @abstractmethod
    def execute(
            self,
            name: ApartmentName,
            description: ApartmentDescription,
            address: ApartmentAddress,
            rent: ApartmentRent
    ) -> Apartment:
        ...


class CreateApartmentUseCaseImpl(CreateApartmentUseCase):
    def __init__(self, apartment_repository: ApartmentRepository):
        self.apartment_repository = apartment_repository

    def execute(
            self,
            name: ApartmentName,
            description: ApartmentDescription,
            address: ApartmentAddress,
            rent: ApartmentRent
    ) -> Apartment:
        apartment = Apartment.create(name=name, description=description, address=address, rent=rent)
        self.apartment_repository.save(apartment)
        return apartment


def new_create_apartment_usecase(apartment_repository: ApartmentRepository) -> CreateApartmentUseCase:
    return CreateApartmentUseCaseImpl(apartment_repository)