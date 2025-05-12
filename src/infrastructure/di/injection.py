from typing import Iterator

from fastapi import Depends
from sqlalchemy.orm import Session

from src.application.repositories import ApartmentRepository, GuestRepository, BookingRepository
from src.application.usecases.apartment.create_apartment_usecase import CreateApartmentUseCase, \
    new_create_apartment_usecase
from src.application.usecases.apartment.delete_apartment_usecase import DeleteApartmentUseCase, \
    new_delete_apartment_usecase
from src.application.usecases.apartment.find_apartment_by_id_usecase import FindApartmentBuIdUseCase, \
    new_find_apartment_by_id_usecase
from src.application.usecases.booking.create_booking_usecase import CreateBookingUseCase, new_create_booking_usecase
from src.application.usecases.booking.delete_booking_usecase import DeleteBookingUseCase, new_delete_booking_usecase
from src.application.usecases.booking.find_booking_by_id_usecase import new_find_booking_by_id_usecase, \
    FindBookingBuIdUseCase
from src.application.usecases.booking.finish_booking_usecase import FinishBookingUseCase, new_finish_booking_usecase
from src.application.usecases.booking.pay_for_booking_usecase import PayForBookingUseCase, new_pay_for_booking_usecase
from src.application.usecases.guest.create_guest_usecase import CreateGuestUseCase, new_create_guest_usecase
from src.application.usecases.guest.delete_guest_usecase import DeleteGuestUseCase, new_delete_guest_usecase
from src.infrastructure.postgres.apartment.repository import new_apartment_repository
from src.infrastructure.postgres.booking.repository import new_booking_repository
from src.infrastructure.postgres.database import SessionLocal
from src.infrastructure.postgres.guest.repository import new_guest_repository


def get_session() -> Iterator[Session]:
    """Get a session from the database."""
    session: Session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def get_guest_repository(session: Session = Depends(get_session)) -> GuestRepository:
    """Get a GuestRepository instance with dependencies injected."""
    return new_guest_repository(session)


def get_apartment_repository(session: Session = Depends(get_session)) -> ApartmentRepository:
    """Get a ApartmentRepository instance with dependencies injected."""
    return new_apartment_repository(session)


def get_booking_repository(session: Session = Depends(get_session)) -> BookingRepository:
    """Get a BookingRepository instance with dependencies injected."""
    return new_booking_repository(session)


def get_create_guest_usecase(guest_repository: GuestRepository = Depends(get_guest_repository)) -> CreateGuestUseCase:
    """Get a CreateGuestUseCase instance with dependencies injected."""
    return new_create_guest_usecase(guest_repository)


def get_delete_guest_usecase(guest_repository: GuestRepository = Depends(get_guest_repository)) -> DeleteGuestUseCase:
    """Get a DeleteGuestUseCase instance with dependencies injected."""
    return new_delete_guest_usecase(guest_repository)


def get_create_apartment_usecase(
        apartment_repository: ApartmentRepository = Depends(get_apartment_repository)
) -> CreateApartmentUseCase:
    """Get a CreateApartmentUseCase instance with dependencies injected."""
    return new_create_apartment_usecase(apartment_repository)


def get_find_apartment_by_id_usecase(
        apartment_repository: ApartmentRepository = Depends(get_apartment_repository)
) -> FindApartmentBuIdUseCase:
    return new_find_apartment_by_id_usecase(apartment_repository)


def get_delete_apartment_usecase(
        apartment_repository: ApartmentRepository = Depends(get_apartment_repository)
) -> DeleteApartmentUseCase:
    """Get a DeleteApartmentUseCase instance with dependencies injected."""
    return new_delete_apartment_usecase(apartment_repository)


def get_create_booking_usecase(
        booking_repository: BookingRepository = Depends(get_booking_repository)
) -> CreateBookingUseCase:
    """Get a CreateBookingUseCase instance with dependencies injected."""
    return new_create_booking_usecase(booking_repository)


def get_delete_booking_usecase(
        booking_repository: BookingRepository = Depends(get_booking_repository)
) -> DeleteBookingUseCase:
    """Get a DeleteBookingUseCase instance with dependencies injected."""
    return new_delete_booking_usecase(booking_repository)


def get_find_booking_by_id_usecase(
        booking_repository: BookingRepository = Depends(get_booking_repository)
) -> FindBookingBuIdUseCase:
    """Get a FindBookingBuIdUseCase instance with dependencies injected."""
    return new_find_booking_by_id_usecase(booking_repository)


def get_finish_booking_usecase(
        booking_repository: BookingRepository = Depends(get_booking_repository)
) -> FinishBookingUseCase:
    """Get a FinishBookingUseCase instance with dependencies injected."""
    return new_finish_booking_usecase(booking_repository)


def get_pay_for_booking_usecase(
        booking_repository: BookingRepository = Depends(get_booking_repository)
) -> PayForBookingUseCase:
    """Get a PayForBookingUseCase instance with dependencies injected."""
    return new_pay_for_booking_usecase(booking_repository)
