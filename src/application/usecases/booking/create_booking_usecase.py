from abc import abstractmethod

from src.application.repositories.booking_repository import BookingRepository
from src.domain.apartment.entities import Apartment
from src.domain.booking.entities import Booking
from src.domain.booking.value_objects import BookingDates
from src.domain.guest.entities import Guest


class CreateBookingUseCase:
    @abstractmethod
    def execute(self, guest: Guest, apartment: Apartment, booking_dates: BookingDates) -> Booking:
        ...


class CreateBookingUseCaseImpl(CreateBookingUseCase):
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def execute(self, guest: Guest, apartment: Apartment, booking_dates: BookingDates) -> Booking:
        booking = Booking.create(guest, apartment, booking_dates)
        self.booking_repository.save(booking)
        return booking


def new_create_booking_usecase(booking_repository: BookingRepository) -> CreateBookingUseCase:
    return CreateBookingUseCaseImpl(booking_repository)
