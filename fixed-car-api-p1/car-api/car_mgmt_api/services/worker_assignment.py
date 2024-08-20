from typing import Iterable

from car_mgmt_api.exceptions import ResourceNotFoundError, DuplicateResourceError
from car_mgmt_api.extensions import db
from car_mgmt_api.models.car import WorkerAssignment
from car_mgmt_api.repositories import worker_assignment_repo


def create(worker_id: int, car_id: int) -> WorkerAssignment:
    try:
        print(get_by_id(car_id=car_id, worker_id=worker_id))
        raise DuplicateResourceError()
    except ResourceNotFoundError:
        worker_assignment = WorkerAssignment(worker_id=worker_id, car_id=car_id)
        worker_assignment_repo.add(worker_assignment)
        worker_assignment_repo.commit()

    return worker_assignment


def delete(car_id: int, worker_id: int) -> None:
    worker_assignment = worker_assignment_repo.get_by_id(
        car_id=car_id, worker_id=worker_id
    )
    worker_assignment_repo.delete(worker_assignment)
    worker_assignment_repo.commit()


def get_by_id(car_id: int, worker_id: int) -> WorkerAssignment:
    worker_assignment = worker_assignment_repo.get_by_id(
        car_id=car_id, worker_id=worker_id
    )
    if worker_assignment is None:
        raise ResourceNotFoundError(
            "WorkerAssignment", car_id=car_id, worker_id=worker_id
        )

    return worker_assignment


def get_all_by_car_id(car_id: int) -> Iterable[WorkerAssignment]:
    return worker_assignment_repo.get_all_by_car_id(car_id=car_id)


def get_all_by_worker_id(worker_id: int) -> Iterable[WorkerAssignment]:
    return worker_assignment_repo.get_all_by_worker_id(worker_id=worker_id)


def commit() -> None:
    db.session.commit()
