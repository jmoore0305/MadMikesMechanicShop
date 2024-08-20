from datetime import datetime
from typing import Iterable

from car_mgmt_api.exceptions import ResourceNotFoundError
from car_mgmt_api.models.car import Car
from car_mgmt_api.repositories import car_repo


def create(car_info: dict) -> Car:
    car = Car(
        vin=car_info["vin"],
        plate_no=car_info["plate_no"],
        state=car_info["state"],
        make=car_info["make"],
        model=car_info["model"],
        year=car_info["year"],
        owner_name=car_info["owner_name"],
        owner_address=car_info["owner_address"],
        owner_dl_number=car_info["owner_dl_number"],
        checkin_at=datetime.now(),
        checkout_at=None
    )

    car_repo.add(car)
    car_repo.commit()

    return car


def update(car_info: dict, car_id: int) -> Car:
    car = get_by_id(car_id)

    car.vin = car_info.get("vin", car.vin)
    car.plate_no = car_info.get("plate_no", car.plate_no)
    car.state = car_info.get("state", car.state)
    car.make = car_info.get("make", car.make)
    car.model = car_info.get("model", car.model)
    car.year = car_info.get("year", car.year)
    car.owner_name = car_info.get("owner_name", car.owner_name)
    car.owner_address = car_info.get("owner_address", car.owner_address)
    car.owner_dl_number = car_info.get("owner_dl_number", car.owner_dl_number)
    car.checkout_at = car_info.get("checkout_at", car.checkout_at)

    car_repo.update(car)
    car_repo.commit()

    return car


def delete(car_id: int) -> None:
    car = get_by_id(car_id)
    car_repo.delete(car)
    car_repo.commit()


def get_by_id(car_id: int) -> Car:
    car = car_repo.get_by_id(car_id)
    if car is None:
        raise ResourceNotFoundError("Car", id=car_id)
    return car


def get_all() -> Iterable[Car]:
    return car_repo.get_all()
