from __future__ import annotations

from src.domain.apartment.value_objects import ApartmentId, ApartmentName, ApartmentDescription, ApartmentAddress, \
    ApartmentRent


class Apartment:
    def __init__(
            self,
            apartment_id: ApartmentId,
            name: ApartmentName,
            description: ApartmentDescription,
            address: ApartmentAddress,
            rent: ApartmentRent
    ):
        self.id = apartment_id

        self._name = name
        self._description = description
        self._address = address
        self._rent = rent

    @property
    def name(self) -> ApartmentName:
        return self._name

    @property
    def description(self) -> ApartmentDescription:
        return self._description

    @property
    def address(self) -> ApartmentAddress:
        return self._address

    @property
    def rent(self) -> ApartmentRent:
        return self._rent

    @property
    def rent_amount(self) -> ApartmentRent:
        return self._rent

    def update_name(self, new_name: ApartmentName) -> None:
        self._name = new_name

    def update_rent(self, new_rent: ApartmentRent) -> None:
        self._rent = new_rent

    def update_description(self, new_description: ApartmentDescription) -> None:
        self._description = new_description

    @staticmethod
    def create(
            name: ApartmentName,
            description: ApartmentDescription,
            address: ApartmentAddress,
            rent: ApartmentRent
    ) -> Apartment:
        return Apartment(ApartmentId.generate(), name, description, address, rent)
