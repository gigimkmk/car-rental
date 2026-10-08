from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.users import User
    from app.models.cars import Car

from datetime import date, datetime

from sqlalchemy import (
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    func
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database import AsyncBase


class Rental(AsyncBase):
    __tablename__ = "rentals"

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

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    end_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    days: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    total_price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="active",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    user: Mapped["User"] = relationship(
        back_populates="rentals"
    )

    car: Mapped["Car"] = relationship(
        back_populates="rentals"
    )