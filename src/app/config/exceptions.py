from rest_framework.exceptions import APIException


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class EntityNotFound(APIException):
    status_code = 404
    default_detail = 'Entity Not Found.'
    default_code = 'entity_not_found'
