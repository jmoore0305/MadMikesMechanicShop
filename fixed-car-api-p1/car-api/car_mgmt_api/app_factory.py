from typing import Optional
from flask import Flask, current_app


def create_app(import_name: str, config: Optional[dict] = None) -> Flask:
    app = Flask(import_name)

    # Load configuration
    if config is not None:
        app.config.from_mapping(config)

    app.url_map.strict_slashes = False

    # Initialize Flask extensions
    from car_mgmt_api.extensions import db, migrate

    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    from car_mgmt_api.blueprints import car_bp, worker_bp, car_assignment_bp

    car_bp.register_blueprint(car_assignment_bp, url_prefix="/<int:car_id>/workers")
    app.register_blueprint(car_bp, url_prefix="/cars")
    app.register_blueprint(worker_bp, url_prefix="/workers")

    # Register exception handlers
    from car_mgmt_api.exceptions import APIError
    from marshmallow.exceptions import ValidationError
    from werkzeug.exceptions import HTTPException, default_exceptions

    def _handle_http_exception(error: HTTPException):
        error_body = {"status": error.code, "detail": error.description}
        current_app.logger.exception(error)
        return error_body, error.code

    @app.errorhandler(ValidationError)
    def handle_validation_error(error: ValidationError):
        current_app.logger.exception(error)
        return error.messages, 422

    @app.errorhandler(APIError)
    def handle_api_exception(error: APIError):
        current_app.logger.exception(error)
        return error.to_dict(), error.status_code

    for http_exception_type in default_exceptions:
        app.errorhandler(http_exception_type)(_handle_http_exception)

    return app
