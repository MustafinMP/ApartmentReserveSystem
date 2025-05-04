from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ApartmentAddress:
    city: str
    street: str
    building_number: str
    apartment_number: Optional[int, None]

    def __str__(self):
        return f'{self.city}, {self.street}, {self.building_number}, {self.apartment_number}'
