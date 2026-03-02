class APIException(Exception):
    status_code = 400
    message = "API error"

    def __init__(self, message=None, status_code=None):
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code
        super().__init__(self.message)


class BadRequest(APIException):
    status_code = 400


class Forbidden(APIException):
    status_code = 403


class InternalServerError(APIException):
    status_code = 500
