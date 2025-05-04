from abc import abstractmethod

from src.domain.entities.apartment import Apartment
from src.domain.entity_values.apartment import ApartmentCost, ApartmentDescription, ApartmentName
from src.domain.entity_values.apartment.apartment_address import ApartmentAddress
from src.domain.repositories import ApartmentRepository


class CreateApartmentUseCase:
    @abstractmethod
    def execute(
            self,
            name: ApartmentName,
            description: ApartmentDescription,
            address: ApartmentAddress,
            cost: ApartmentCost
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
            cost: ApartmentCost
    ) -> Apartment:
        apartment = Apartment.create(name=name, description=description, address=address, cost=cost)
        self.apartment_repository.save(apartment)
        return apartment


def new_create_apartment_usecase(apartment_repository: ApartmentRepository) -> CreateApartmentUseCase:
    return CreateApartmentUseCaseImpl(apartment_repository)