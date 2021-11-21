from rest_framework.exceptions import APIException


class WrongDateFormat(APIException):
    status_code = 422
    default_detail = 'Wrong date format : Please follow this format: YYYY-MM-DD'
