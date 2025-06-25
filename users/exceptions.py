from rest_framework.exceptions import APIException
from rest_framework import status

class InvalidPasswordException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_code = 'invalid_password'

    def __init__(self, detail=None):
        if detail is None:
            detail = {"parol": ["Parol noto'g'ri"]}
        detail["status_code"] = self.status_code
        super().__init__(detail=detail)
