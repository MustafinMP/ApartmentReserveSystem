from dataclasses import dataclass


@dataclass(frozen=True)
class GuestFullname:
    value: str

