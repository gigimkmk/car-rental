from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.users import User
    from app.models.cars import Car

from sqlalchemy import (
    ForeignKey,
    Integer,
    UniqueConstraint
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database import AsyncBase


class Like(AsyncBase):
    __tablename__ = "likes"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "car_id",
            name="unique_user_car_like"
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    car_id: Mapped[int] = mapped_column(
        ForeignKey("cars.id"),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates="likes"
    )

    car: Mapped["Car"] = relationship(
        back_populates="likes"
    )