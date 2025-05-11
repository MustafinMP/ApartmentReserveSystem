from abc import abstractmethod

from src.application.repositories import BookingRepository
from src.domain.booking.entities import Booking
from src.domain.booking.exceptions import BookingNotFound, BookingIsNotPayed
from src.domain.booking.value_objects import BookingId


class FinishBookingUseCase:
    @abstractmethod
    def execute(self, booking_id: BookingId) -> Booking:
        ...


class FinishBookingUseCaseImpl(FinishBookingUseCase):
    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def execute(self, booking_id: BookingId) -> Booking:
        booking = self.repository.find_by_id(booking_id)

        if booking is None:
            raise BookingNotFound

        try:
            booking.finish()
            self.repository.save(booking)
            return booking
        except BookingIsNotPayed:
            raise BookingIsNotPayed


def new_finish_booking_usecase(booking_repository: BookingRepository) -> FinishBookingUseCase:
    return FinishBookingUseCaseImpl(booking_repository)
