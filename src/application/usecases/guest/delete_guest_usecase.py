from abc import abstractmethod

from src.application.repositories.guest_repository import GuestRepository
from src.domain.guest.exceptions import GuestNotFound
from src.domain.guest.value_objects import GuestId


class DeleteGuestUseCase:
    @abstractmethod
    def execute(self, guest_id: GuestId) -> None:
        ...


class DeleteGuestUseCaseImpl(DeleteGuestUseCase):
    def __init__(self, guest_repository: GuestRepository):
        self.guest_repository = guest_repository

    def execute(self, guest_id: GuestId) -> None:
        guest = self.guest_repository.find_by_id(guest_id)

        if guest is None:
            raise GuestNotFound

        self.guest_repository.delete(guest_id)


def new_delete_guest_usecase(guest_repository: GuestRepository) -> DeleteGuestUseCase:
    return DeleteGuestUseCaseImpl(guest_repository)
