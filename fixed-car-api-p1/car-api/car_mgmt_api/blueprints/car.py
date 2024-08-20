from flask import Blueprint, request
from car_mgmt_api.schemas.car import (
    create_car_schema, update_car_schema, car_for_public_schema
)
from car_mgmt_api.services import car_service


car_bp = Blueprint("car", __name__)


@car_bp.route("/", methods=["POST"], endpoint="create")
def handle_create_car():
    car_info = create_car_schema.load(request.json)
    car = car_service.create(car_info=car_info)
    return {"car": car_for_public_schema.dump(car)}


@car_bp.route("/<int:car_id>", methods=["PUT"], endpoint="update")
def handle_update_car(car_id: int):
    car_info = update_car_schema.load(request.json)
    car = car_service.update(car_info=car_info, car_id=car_id)
    return {"car": car_for_public_schema.dump(car)}


@car_bp.route("/<int:car_id>", methods=["GET"], endpoint="read")
def handle_read_car(car_id: int):
    car = car_service.get_by_id(car_id)
    return {"car": car_for_public_schema.dump(car)}


@car_bp.route("/", methods=["GET"], endpoint="list")
def handle_list_cars():
    cars = car_service.get_all()
    return {"cars": car_for_public_schema.dump(cars, many=True)}


@car_bp.route("/<int:car_id>", methods=["DELETE"], endpoint="delete")
def handle_delete_car(car_id: int):
    car_service.delete(car_id)
    return {"message": "Successfully deleted car!"}
