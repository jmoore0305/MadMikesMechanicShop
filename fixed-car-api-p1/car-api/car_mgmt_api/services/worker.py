from typing import Iterable

from car_mgmt_api.exceptions import ResourceNotFoundError
from car_mgmt_api.models.car import Worker
from car_mgmt_api.repositories import worker_repo


def create(name: str) -> Worker:
    worker = Worker(name=name)

    worker_repo.add(worker)
    worker_repo.commit()

    return worker


def update(name: str, worker_id: int) -> Worker:
    worker = get_by_id(worker_id)
    worker.name = name

    worker_repo.update(worker)
    worker_repo.commit()

    return worker


def delete(worker_id: int) -> None:
    worker = get_by_id(worker_id)
    worker_repo.delete(worker)
    worker_repo.commit()


def get_by_id(worker_id: int) -> Worker:
    worker = worker_repo.get_by_id(worker_id)
    if worker is None:
        raise ResourceNotFoundError("Worker", id=worker_id)
    return worker


def get_all() -> Iterable[Worker]:
    return worker_repo.get_all()
