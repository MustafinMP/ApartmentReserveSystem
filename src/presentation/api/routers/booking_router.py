from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status
from starlette.exceptions import HTTPException

from src.application.usecases.apartment.find_apartment_by_id_usecase import FindApartmentBuIdUseCase
from src.application.usecases.booking.create_booking_usecase import CreateBookingUseCase
from src.application.usecases.booking.delete_booking_usecase import DeleteBookingUseCase
from src.application.usecases.booking.find_booking_by_id_usecase import FindBookingBuIdUseCase
from src.application.usecases.booking.finish_booking_usecase import new_finish_booking_usecase
from src.application.usecases.booking.pay_for_booking_usecase import PayForBookingUseCase, new_pay_for_booking_usecase
from src.domain.booking.exceptions import BookingNotFound
from src.domain.booking.value_objects import BookingId, BookingDates
from src.infrastructure.di.injection import get_create_booking_usecase, get_find_booking_by_id_usecase, \
    get_delete_booking_usecase, get_find_apartment_by_id_usecase
from src.presentation.api.schemas.booking_schema import CreateBookingSchema, BookingSchema

router = APIRouter(
    prefix='/booking',
    tags=['booking']
)



@router.post('/')
async def create_booking(
        booking_data: CreateBookingSchema,
        usecase: CreateBookingUseCase = Depends(get_create_booking_usecase)
):
    booking = usecase.execute(
        apartment=booking_data.apartment.to_entity(),
        guest=booking_data.guest.to_entity(),
        booking_dates=BookingDates(
            booking_data.date_from,
            booking_data.date_to
        )
    )
    return BookingSchema.from_entity(booking)


@router.get('/{booking_id}')
async def get_booking_by_id(
        booking_id: UUID,
        usecase: FindBookingBuIdUseCase = Depends(get_find_booking_by_id_usecase)
):
    try:
        booking = usecase.execute(BookingId(booking_id))
        return BookingSchema.from_entity(booking)
    except BookingNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )


@router.put('/pay/{booking_id}')
async def pay_for_booking(
        booking_id: UUID,
        usecase: PayForBookingUseCase = Depends(new_pay_for_booking_usecase)
):
    try:
        booking = usecase.execute(BookingId(booking_id))
        return BookingSchema.from_entity(booking)
    except BookingNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )


@router.put('/finish/{booking_id}')
async def finish_booking(
        booking_id: UUID,
        usecase: FindBookingBuIdUseCase = Depends(new_finish_booking_usecase)
):
    try:
        booking = usecase.execute(BookingId(booking_id))
        return BookingSchema.from_entity(booking)
    except BookingNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )


@router.delete('/{booking_id}')
async def delete_booking(
        booking_id: str,
        usecase: DeleteBookingUseCase = Depends(get_delete_booking_usecase)
):
    usecase.execute(BookingId(booking_id))
