from marshmallow import Schema, fields


class CreateWorkerSchema(Schema):
    name = fields.String(required=True)


class UpdateWorkerSchema(Schema):
    name = fields.String(required=True)


class WorkerForPublicSchema(Schema):
    id = fields.Integer()
    name = fields.String()


create_worker_schema = CreateWorkerSchema()
update_worker_schema = UpdateWorkerSchema()
worker_for_public_schema = WorkerForPublicSchema()
