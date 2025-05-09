from typing import Iterator

from fastapi import Depends
from sqlalchemy.orm import Session

from src.application.repositories import ApartmentRepository, GuestRepository
from src.application.usecases.apartment.create_apartment_usecase import CreateApartmentUseCase, \
    new_create_apartment_usecase
from src.application.usecases.apartment.delete_apartment_usecase import DeleteApartmentUseCase, \
    new_delete_apartment_usecase
from src.application.usecases.apartment.find_apartment_by_id_usecase import FindApartmentBuIdUseCase, \
    new_find_apartment_by_id_usecase
from src.application.usecases.guest.create_guest_usecase import CreateGuestUseCase, new_create_guest_usecase
from src.application.usecases.guest.delete_guest_usecase import DeleteGuestUseCase, new_delete_guest_usecase
from src.infrastructure.postgres.apartment.repository import new_apartment_repository
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
