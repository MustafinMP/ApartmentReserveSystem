from abc import abstractmethod

from src.domain.entity_values.apartment import ApartmentId
from src.domain.exceptions import ApartmentNotFound
from src.domain.repositories import ApartmentRepository


class DeleteApartmentUseCase:
    @abstractmethod
    def execute(self, apartment_id: ApartmentId) -> None:
        ...


class DeleteApartmentUseCaseImpl(DeleteApartmentUseCase):
    def __init__(self, apartment_repository: ApartmentRepository):
        self.apartment_repository = apartment_repository

    def execute(self, apartment_id: ApartmentId) -> None:
        apartment = self.apartment_repository.find_by_id(apartment_id)

        if apartment is None:
            raise ApartmentNotFound

        self.apartment_repository.delete(apartment_id)


def new_delete_apartment_usecase(apartment_repository: ApartmentRepository) -> DeleteApartmentUseCase:
    return DeleteApartmentUseCaseImpl(apartment_repository)