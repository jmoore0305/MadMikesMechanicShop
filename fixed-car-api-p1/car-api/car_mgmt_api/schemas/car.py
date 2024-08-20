from marshmallow import Schema, fields


class CreateCarSchema(Schema):
    vin = fields.String(required=True)
    plate_no = fields.String(required=True)
    state = fields.String(required=True)
    make = fields.String(required=True)
    model = fields.String(required=True)
    year = fields.Integer(required=True)
    owner_name = fields.String(required=True)
    owner_address = fields.String(required=True)
    owner_dl_number = fields.String(required=True)


class UpdateCarSchema(Schema):
    vin = fields.String()
    plate_no = fields.String()
    state = fields.String()
    make = fields.String()
    model = fields.String()
    year = fields.Integer()
    owner_name = fields.String()
    owner_address = fields.String()
    owner_dl_number = fields.String()
    checkout_at = fields.DateTime()


class CarForPublicSchema(Schema):
    id = fields.Integer()
    vin = fields.String()
    plate_no = fields.String()
    state = fields.String()
    make = fields.String()
    model = fields.String()
    year = fields.Integer()
    owner_name = fields.String()
    owner_address = fields.String()
    owner_dl_number = fields.String()
    checkin_at = fields.DateTime()
    checkout_at = fields.DateTime()


create_car_schema = CreateCarSchema()
update_car_schema = UpdateCarSchema()
car_for_public_schema = CarForPublicSchema()
