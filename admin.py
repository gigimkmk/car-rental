from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.users import User
from app.models.cars import Car
from app.models.rentals import Rental
from app.models.likes import Like

from app.schemas.users import UserResponse
from app.schemas.cars import CarResponse
from app.schemas.rentals import RentalResponse
from app.security import get_current_admin


router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Depends(get_current_admin)]
)


@router.get("/users", response_model=list[UserResponse])
async def get_all_users(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(User).order_by(User.id)
    )

    return result.scalars().all()


@router.get("/cars", response_model=list[CarResponse])
async def get_all_cars(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Car).order_by(Car.id)
    )

    return result.scalars().all()


@router.get("/rentals", response_model=list[RentalResponse])
async def get_all_rentals(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Rental).order_by(Rental.id)
    )

    return result.scalars().all()


@router.delete("/cars/{car_id}")
async def delete_car(
    car_id: int,
    db: AsyncSession = Depends(get_db)
):
    car = await db.get(Car, car_id)

    if car is None:
        raise HTTPException(
            status_code=404,
            detail="Car not found"
        )

    rentals_result = await db.execute(
        select(Rental.id)
        .where(Rental.car_id == car_id)
        .limit(1)
    )

    if rentals_result.scalar_one_or_none() is not None:
        raise HTTPException(
            status_code=409,
            detail="Cannot delete a car with rental history"
        )

    likes_result = await db.execute(
        select(Like).where(Like.car_id == car_id)
    )

    for like in likes_result.scalars().all():
        await db.delete(like)

    await db.delete(car)
    await db.commit()

    return {
        "message": "Car deleted successfully"
    }