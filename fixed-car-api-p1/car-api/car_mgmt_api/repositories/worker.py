from typing import Optional, Iterable

from car_mgmt_api.extensions import db
from car_mgmt_api.models.car import Worker


def add(worker: Worker) -> None:
    db.session.add(worker)


def update(worker: Worker) -> None:
    db.session.add(worker)


def delete(worker: Worker) -> None:
    db.session.delete(worker)


def get_by_id(worker_id: int) -> Optional[Worker]:
    return Worker.query.get(worker_id)


def get_all() -> Iterable[Worker]:
    return Worker.query.all()


def commit() -> None:
    db.session.commit()
