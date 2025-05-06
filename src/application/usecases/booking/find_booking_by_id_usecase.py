from abc import abstractmethod

from src.application.repositories.booking_repository import BookingRepository
from src.domain.booking.entities import Booking
from src.domain.booking.exceptions import BookingNotFound
from src.domain.booking.value_objects import BookingId


class FindBookingBuIdUseCase:
    @abstractmethod
    def execute(self, booking_id: BookingId) -> Booking:
        ...


class FindBookingBuIdUseCaseImpl(FindBookingBuIdUseCase):
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def execute(self, booking_id: BookingId) -> Booking:
        booking = self.booking_repository.find_by_id(booking_id)

        if booking is None:
            raise BookingNotFound

        return booking


def new_find_booking_by_id_usecase(booking_repository: BookingRepository) -> FindBookingBuIdUseCase:
    return FindBookingBuIdUseCaseImpl(booking_repository)