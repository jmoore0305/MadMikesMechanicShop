from typing import Optional, Iterable

from car_mgmt_api.extensions import db
from car_mgmt_api.models.car import WorkerAssignment


def add(worker_assignment: WorkerAssignment) -> None:
    db.session.add(worker_assignment)


def delete(worker_assignment: WorkerAssignment) -> None:
    db.session.delete(worker_assignment)


def get_by_id(car_id: int, worker_id: int) -> Optional[WorkerAssignment]:
    return WorkerAssignment.query \
        .filter_by(car_id=car_id) \
        .filter_by(worker_id=worker_id) \
        .first()


def get_all_by_car_id(car_id: int) -> Iterable[WorkerAssignment]:
    return WorkerAssignment.query.filter_by(car_id=car_id).all()


def get_all_by_worker_id(worker_id: int) -> Iterable[WorkerAssignment]:
    return WorkerAssignment.query.filter_by(worker_id=worker_id).all()


def commit() -> None:
    db.session.commit()
