from abc import abstractmethod

from src.application.repositories.guest_repository import GuestRepository
from src.domain.guest.entities import Guest
from src.domain.guest.value_objects import GuestFullname, GuestPhoneNumber


class CreateGuestUseCase:
    @abstractmethod
    def execute(self, fullname: GuestFullname, phone_number: GuestPhoneNumber) -> Guest:
        ...


class CreateGuestUseCaseImpl(CreateGuestUseCase):
    def __init__(self, guest_repository: GuestRepository):
        self.guest_repository = guest_repository

    def execute(self, fullname: GuestFullname, phone_number: GuestPhoneNumber) -> Guest:
        guest = Guest.create(fullname, phone_number)
        self.guest_repository.save(guest)
        return guest


def new_create_guest_usecase(guest_repository: GuestRepository) -> CreateGuestUseCase:
    return CreateGuestUseCaseImpl(guest_repository)
