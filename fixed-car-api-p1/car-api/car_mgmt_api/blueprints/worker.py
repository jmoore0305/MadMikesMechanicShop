from flask import Blueprint, request
from car_mgmt_api.schemas.worker import (
    create_worker_schema, update_worker_schema, worker_for_public_schema
)
from car_mgmt_api.schemas.car_assignment import car_assignment_for_public_schema
from car_mgmt_api.services import worker_service, worker_assignment_service


worker_bp = Blueprint("worker", __name__)


@worker_bp.route("/", methods=["POST"], endpoint="create")
def handle_create_worker():
    worker_info = create_worker_schema.load(request.json)
    worker = worker_service.create(name=worker_info["name"])
    return {"worker": worker_for_public_schema.dump(worker)}



@worker_bp.route("/<int:worker_id>", methods=["PUT"], endpoint="update")
def handle_update_worker(worker_id: int):
    worker_info = update_worker_schema.load(request.json)
    worker = worker_service.update(name=worker_info["name"], worker_id=worker_id)
    return {"worker": worker_for_public_schema.dump(worker)}


@worker_bp.route("/<int:worker_id>", methods=["GET"], endpoint="read")
def handle_read_worker(worker_id: int):
    worker = worker_service.get_by_id(worker_id=worker_id)
    return {"worker": worker_for_public_schema.dump(worker)}


@worker_bp.route("/<int:worker_id>/cars", methods=["GET"], endpoint="read_assignments")
def handle_read_assigned_cars(worker_id: int):
    worker_assignments = worker_assignment_service.get_all_by_worker_id(worker_id)
    return {"assignments": car_assignment_for_public_schema.dump(worker_assignments, many=True)}


@worker_bp.route("/", methods=["GET"], endpoint="list")
def handle_list_workers():
    workers = worker_service.get_all()
    return {"workers": worker_for_public_schema.dump(workers, many=True)}


@worker_bp.route("/<int:worker_id>", methods=["DELETE"], endpoint="delete")
def handle_delete_worker(worker_id: int):
    worker_service.delete(worker_id)
    return {"message": "Successfully deleted worker!"}
