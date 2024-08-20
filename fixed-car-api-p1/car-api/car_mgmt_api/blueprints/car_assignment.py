from flask import Blueprint, request
from car_mgmt_api.schemas.car_assignment import (
    create_car_assignment_schema, car_assignment_for_public_schema
)
from car_mgmt_api.services import worker_assignment_service


car_assignment_bp = Blueprint("car_assignment", __name__)


@car_assignment_bp.route("/", methods=["POST"], endpoint="create")
def handle_create_car_assignment(car_id: int):
    car_assignment_info = create_car_assignment_schema.load(request.json)
    car_assignment = worker_assignment_service.create(
        car_id=car_id, worker_id=car_assignment_info["worker_id"]
    )
    return {"assignment": car_assignment_for_public_schema.dump(car_assignment)}


@car_assignment_bp.route("/", methods=["GET"], endpoint="list")
def handle_list_car_assignments(car_id: int):
    car_assignments = worker_assignment_service.get_all_by_car_id(car_id=car_id)
    return {"assignments": car_assignment_for_public_schema.dump(car_assignments, many=True)}


@car_assignment_bp.route("/<int:worker_id>", methods=["DELETE"], endpoint="delete")
def handle_delete_car_assignment(car_id: int, worker_id: int):
    worker_assignment_service.delete(car_id=car_id, worker_id=worker_id)
    return {"message": "Successfully deleted car_assignment!"}
