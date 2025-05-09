from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status
from starlette.exceptions import HTTPException

from src.application.usecases.apartment.create_apartment_usecase import CreateApartmentUseCase
from src.application.usecases.apartment.delete_apartment_usecase import DeleteApartmentUseCase
from src.application.usecases.apartment.find_apartment_by_id_usecase import FindApartmentBuIdUseCase
from src.domain.apartment.exceptions import ApartmentNotFound
from src.domain.apartment.value_objects import ApartmentId, ApartmentName, ApartmentDescription, ApartmentAddress, \
    ApartmentRent
from src.infrastructure.di.injection import get_find_apartment_by_id_usecase, get_delete_apartment_usecase, \
    get_create_apartment_usecase
from src.presentation.api.schemas import ApartmentSchema
from src.presentation.api.schemas.apartment_schema import CreateApartmentSchema

router = APIRouter(
    prefix='/apartment',
    tags=['apartment']
)


@router.post('/')
async def create_apartment(
        apartment_data: CreateApartmentSchema,
        usecase: CreateApartmentUseCase = Depends(get_create_apartment_usecase)
):
    apartment = usecase.execute(
        ApartmentName(apartment_data.name),
        ApartmentDescription(apartment_data.description),
        ApartmentAddress(apartment_data.address),
        ApartmentRent(apartment_data.rent)
    )
    return ApartmentSchema.from_entity(apartment)


@router.get('/{apartment_id}')
async def get_apartment_by_id(
        apartment_id: UUID,
        usecase: FindApartmentBuIdUseCase = Depends(get_find_apartment_by_id_usecase)
):
    try:
        apartment = usecase.execute(ApartmentId(apartment_id))
        return ApartmentSchema.from_entity(apartment)
    except ApartmentNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )


@router.delete('/{apartment_id}')
async def delete_apartment(
        apartment_id: str,
        usecase: DeleteApartmentUseCase = Depends(get_delete_apartment_usecase)
):
    usecase.execute(ApartmentId(apartment_id))
