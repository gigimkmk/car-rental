from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    DateTime,
    Integer,
    String,
    func,
    text
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import AsyncBase


if TYPE_CHECKING:
    from app.models.cars import Car
    from app.models.rentals import Rental
    from app.models.likes import Like


class User(AsyncBase):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    first_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    phone_number: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    is_admin: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default=text("false")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    cars: Mapped[list["Car"]] = relationship(
        back_populates="owner"
    )

    rentals: Mapped[list["Rental"]] = relationship(
        back_populates="user"
    )

    likes: Mapped[list["Like"]] = relationship(
        back_populates="user"
    )