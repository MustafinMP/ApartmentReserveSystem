from __future__ import annotations

from src.domain.entity_values.apartment import ApartmentId, ApartmentAddress, ApartmentName, ApartmentDescription, \
    ApartmentCost


class Apartment:
    def __init__(
            self,
            apartment_id: ApartmentId,
            name: ApartmentName,
            description: ApartmentDescription,
            address: ApartmentAddress,
            cost: ApartmentCost
    ):
        self.id = apartment_id

        self._name = name
        self._description = description
        self._address = address
        self._cost = cost

    @property
    def name(self) -> ApartmentName:
        return self._name

    @property
    def cost(self) -> ApartmentCost:
        return self._cost

    @staticmethod
    def create(
            name: ApartmentName,
            description: ApartmentDescription,
            address: ApartmentAddress,
            cost: ApartmentCost
    ) -> Apartment:
        return Apartment(ApartmentId.generate(), name, description, address, cost)
