from abc import abstractmethod

from src.application.repositories import BookingRepository
from src.domain.booking.exceptions import BookingNotFound
from src.domain.booking.value_objects import BookingId


class DeleteBookingUseCase:
    @abstractmethod
    def execute(self, booking_id: BookingId) -> None:
        ...


class DeleteBookingUseCaseImpl(DeleteBookingUseCase):
    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def execute(self, booking_id: BookingId) -> None:
        booking = self.repository.find_by_id(booking_id)

        if booking is None:
            raise BookingNotFound

        self.repository.delete(booking_id)


def new_delete_booking_usecase(booking_repository: BookingRepository) -> DeleteBookingUseCase:
    return DeleteBookingUseCaseImpl(booking_repository)
