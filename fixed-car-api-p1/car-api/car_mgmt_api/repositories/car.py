from typing import Optional, Iterable

from car_mgmt_api.extensions import db
from car_mgmt_api.models.car import Car


def add(car: Car) -> None:
    db.session.add(car)


def update(car: Car) -> None:
    db.session.add(car)


def delete(car: Car) -> None:
    db.session.delete(car)


def get_by_id(car_id: int) -> Optional[Car]:
    return Car.query.get(car_id)


def get_all() -> Iterable[Car]:
    return Car.query.all()


def commit() -> None:
    db.session.commit()
