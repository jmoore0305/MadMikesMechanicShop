from marshmallow import Schema, fields


class CreateCarAssignmentSchema(Schema):
    worker_id = fields.Integer(required=True)


class CarAssignmentForPublicSchema(Schema):
    car_id = fields.Integer()
    worker_id = fields.Integer()


create_car_assignment_schema = CreateCarAssignmentSchema()
car_assignment_for_public_schema = CarAssignmentForPublicSchema()
