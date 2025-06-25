from rest_framework.exceptions import APIException
from rest_framework import status

class InvalidPasswordException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_code = 'invalid_password'

    def __init__(self, detail=None):
        if detail is None:
            detail = {"parol": ["Parol noto'g'ri"]}

        detail["status_code"] = int(self.status_code)

        self.detail = detail

class PasswordMismatchException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'password_mismatch'

    def __init__(self, detail=None):
        if detail is None:
            detail = {"parol": ["Parollar mos emas tekshirib qaytadan kiriting"]}
        detail["status_code"] = int(self.status_code)

        self.detail = detail
    
class EmailAlreadyExistsException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'email_exists'

    def __init__(self, detail=None):
        if detail is None:
            detail = {"User": ["Bu email allaqachon ro'yhatdan o'tkan"]}
        detail["status_code"] = int(self.status_code)

        self.detail = detail
    
class DisabilityRequiredException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'disability_required'

    def __init__(self, detail=None):
        if detail is None:
            detail = {"Error": ["O'quvchilar uchun nogironlikni tanlash majburiy"]}
        detail["status_code"] = int(self.status_code)

        self.detail = detail
class UserNotFoundException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'user_not_found'

    def __init__(self, detail=None):
        if detail is None:
            detail = {
                "User": ["Bunday foydalanuvchi mavjud emas"]
            }
        detail["status_code"] = int(self.status_code)

        self.detail = detail
    
class NewPasswordMismatchException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'new_password_mismatch'

    def __init__(self, detail=None):
        if detail is None:
            detail = {
                "error": "Yangi parollar mos emas!"
            }
        detail["status_code"] = int(self.status_code)

        self.detail = detail

class OldPasswordIncorrectException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'old_password_incorrect'

    def __init__(self, detail=None):
        if detail is None:
            detail = {
                "error": "Eski parol noto'g'ri kiritilgan"
            }
        detail["status_code"] = int(self.status_code)

        self.detail = detail