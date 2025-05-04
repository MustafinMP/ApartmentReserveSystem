from dataclasses import dataclass


@dataclass(frozen=True)
class GuestPhoneNumber:
    value: str

