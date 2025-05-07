from __future__ import annotations

from src.domain.guest.value_objects import GuestId, GuestFullname, GuestPhoneNumber


class Guest:
    def __init__(
            self,
            guest_id: GuestId,
            fullname: GuestFullname,
            phone_number: GuestPhoneNumber
    ):
        self._id = guest_id
        self._fullname = fullname
        self._phone_number = phone_number

    @property
    def id(self) -> GuestId:
        return self._id

    @property
    def fullname(self) -> GuestFullname:
        return self._fullname

    @property
    def phone_number(self) -> GuestPhoneNumber:
        return self._phone_number

    @staticmethod
    def create(
            fullname: GuestFullname,
            phone_number: GuestPhoneNumber
    ) -> Guest:
        return Guest(GuestId.generate(), fullname, phone_number)
