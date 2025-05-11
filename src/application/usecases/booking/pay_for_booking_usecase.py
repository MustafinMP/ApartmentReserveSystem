from abc import abstractmethod

from src.application.repositories import BookingRepository
from src.domain.booking.entities import Booking
from src.domain.booking.exceptions import BookingNotFound
from src.domain.booking.value_objects import BookingId


class PayForBookingUseCase:
    @abstractmethod
    def execute(self, booking_id: BookingId) -> Booking:
        ...


class PayForBookingUseCaseImpl(PayForBookingUseCase):
    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def execute(self, booking_id: BookingId) -> Booking:
        booking = self.repository.find_by_id(booking_id)

        if booking is None:
            raise BookingNotFound

        booking.pay()
        self.repository.save(booking)
        return booking


def new_pay_for_booking_usecase(booking_repository: BookingRepository) -> PayForBookingUseCase:
    return PayForBookingUseCaseImpl(booking_repository)
