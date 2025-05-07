from __future__ import annotations

from uuid import UUID

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.guest.entities import Guest
from src.domain.guest.value_objects import GuestFullname, GuestPhoneNumber, GuestId
from src.infrastructure.postgres.database import Base


class GuestModel(Base):
    __tablename__ = 'guest'

    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=False)
    fullname: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)

    def to_entity(self) -> Guest:
        return Guest(
            guest_id=GuestId(self.id),
            fullname=GuestFullname(self.fullname),
            phone_number=GuestPhoneNumber(self.phone_number)
        )

    @staticmethod
    def from_entity(guest: Guest) -> GuestModel:
        return GuestModel(
            id=guest.id.value,
            fullname=guest.fullname.value,
            phone_number=guest.phone_number.value
        )
