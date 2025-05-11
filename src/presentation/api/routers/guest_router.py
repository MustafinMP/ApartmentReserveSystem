from uuid import UUID

from fastapi import APIRouter, Depends

from src.application.usecases.guest.create_guest_usecase import CreateGuestUseCase
from src.application.usecases.guest.delete_guest_usecase import DeleteGuestUseCase
from src.domain.guest.value_objects import GuestId, GuestFullname, GuestPhoneNumber
from src.infrastructure.di.injection import get_create_guest_usecase, get_delete_guest_usecase
from src.presentation.api.schemas.guest_schema import CreateGuestSchema, GuestSchema

router = APIRouter(
    prefix='/guest',
    tags=['guest']
)


@router.post('/')
async def create_guest(
        guest_data: CreateGuestSchema,
        usecase: CreateGuestUseCase = Depends(get_create_guest_usecase)
):
    guest = usecase.execute(
        GuestFullname(guest_data.fullname),
        GuestPhoneNumber(guest_data.phone_number)
    )
    return GuestSchema.from_entity(guest)


@router.get('/all')
async def get_all_guests(
        apartment_id: UUID,
):
    return 0


@router.delete('/{guest_id}')
async def delete_guest(
        guest_id: str,
        usecase: DeleteGuestUseCase = Depends(get_delete_guest_usecase)
):
    usecase.execute(GuestId(guest_id))
