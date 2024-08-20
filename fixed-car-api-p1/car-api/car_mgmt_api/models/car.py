from car_mgmt_api.extensions import db


class Car(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.String, nullable=False)
    plate_no = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    owner_name = db.Column(db.String, nullable=False)
    owner_address = db.Column(db.String, nullable=False)
    owner_dl_number = db.Column(db.String, nullable=False)
    checkin_at = db.Column(db.DateTime, nullable=True)
    checkout_at = db.Column(db.DateTime, nullable=True)


class Worker(db.Model):
    __tablename__ = "workers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)


class WorkerAssignment(db.Model):
    __tablename__ = "worker_assignment"
    worker_id = db.Column(
        db.Integer,
        db.ForeignKey("workers.id"),
        primary_key=True,
        nullable=False
    )
    car_id = db.Column(
        db.Integer,
        db.ForeignKey("cars.id"),
        primary_key=True,
        nullable=False
    )
