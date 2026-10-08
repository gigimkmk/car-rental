from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import app.models

from app.database import (
    AsyncBase,
    engine
)

from app.routers import (
    cars,
    likes,
    rentals,
    users
)


app = FastAPI(
    title="Car Rental Portal API",
    version="1.0.0"
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as connection:
        await connection.run_sync(
            AsyncBase.metadata.create_all
        )


app.include_router(
    users.router
)

app.include_router(
    cars.router
)

app.include_router(
    rentals.router
)

app.include_router(
    likes.router
)


app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)


@app.get("/")
async def root():
    return {
        "message": "Car Rental Portal API is running"
    }