from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.users import User
    from app.models.rentals import Rental
    from app.models.likes import Like


from datetime import datetime

from sqlalchemy import (
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    DateTime,
    func
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database import AsyncBase


class Car(AsyncBase):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    brand: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    model: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    price_per_day: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    capacity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    transmission: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    city: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    fuel_tank_capacity: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    image1: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    image2: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    image3: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    latitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    longitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    owner: Mapped["User"] = relationship(
        back_populates="cars"
    )

    rentals: Mapped[list["Rental"]] = relationship(
        back_populates="car"
    )

    likes: Mapped[list["Like"]] = relationship(
        back_populates="car"
    )