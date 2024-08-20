from typing import Optional


class APIError(Exception):
    status_code: int = 500
    message: str = "Unexpected Server Error."

    def __init__(
        self, message=None, status_code: Optional[int] = None, detail=None
    ):
        super().__init__()

        if message is not None:
            self.message = message

        if status_code is not None:
            self.status_code = status_code

        self.detail = detail

    def to_dict(self) -> dict:
        body = {"status": self.status_code, "message": self.message}

        if self.detail is not None:
            body["detail"] = self.detail

        return body


class ResourceNotFoundError(APIError):
    model_name: str = "Resource"
    status_code = 404

    def __init__(self, model_name: Optional[str]=None, **kwargs):
        if model_name is None:
            model_name = self.model_name

        model_name = model_name[0].upper() + model_name[1:]
        model_keys = ", ".join(f"{k}={v}" for k, v in kwargs.items())

        if model_keys != "":
            model = f"{model_name}({model_keys})"
        else:
            model = model_name

        super().__init__(message=f"{model} not found!")


class DuplicateResourceError(APIError):
    status_code = 409
    message = "Resource already exists."
