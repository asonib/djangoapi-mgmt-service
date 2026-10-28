from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from rest_framework import status

class PayloadTooLargeException(APIException):
    status_code = status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
    default_detail = 'File size exceeds maximum allowed limit.'
    default_code = 'file_too_large'

class UnsupportedFileTypeException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'File type is not permitted.'
    default_code = 'invalid_file_type'

class ResourceNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Requested resource not found.'
    default_code = 'not_found'

class ForbiddenOperationException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'You do not have permission to perform this operation.'
    default_code = 'forbidden'

def custom_exception_handler(exc, context):
    return exception_handler(exc, context)
