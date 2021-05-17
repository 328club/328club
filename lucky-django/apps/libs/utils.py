import logging

from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import exceptions, status
from rest_framework import status as status_
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import set_rollback

logger = logging.getLogger('django')


class ApiBaseException(Exception):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = '服务出现错误'
    default_code = 'error'

    def __init__(self, detail=None, code=None):
        self.detail = detail or self.default_detail
        self.code = code or self.default_code


def api_fail(code, message, response_status=400, **kwargs):
    from rest_framework.response import Response
    assert code != 200, 'statusCode 不能等于200'
    return Response({
        'statusCode': code,
        'comments': message
    }, status=response_status, **kwargs)


def api_success(data, comments='成功', status=status_.HTTP_200_OK, **kwargs):
    from rest_framework.response import Response
    return Response({
        'statusCode': 200,
        'data': data,
        'comments': comments,
    }, status=status, **kwargs)


def restful_exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()
    #
    # if isinstance(exc, OperateError):
    #     exc = exceptions.APIException(detail=str(exc))

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc, AuthenticationFailed):
            data = {
                'errorCode': 10403,
                'statusCode': -exc.status_code or -1,
                'comments': str(exc)
            }
        elif isinstance(exc.detail, (list, dict)):
            data = {
                'statusCode': -exc.status_code or -1,
                'comments': str(exc),
                # 'messageData': exc.detail
            }

        else:
            data = {
                'statusCode': -exc.status_code or -1,
                'comments': str(exc)
            }

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)
    elif isinstance(exc, ApiBaseException):
        logger.exception(exc)
        msg = exc.detail
        data = {
            'statusCode': exc.status_code,
            'comments': msg
        }
        return Response(data, status=exc.status_code, headers={})
    elif isinstance(exc, Exception):
        logger.exception(exc)
        data = {
            'statusCode': 500,
            'comments': '操作错误！',
            'exception': '{}: {}'.format(exc.__class__.__name__, exc.__str__())
        }
        return Response(data, status=400, headers={})
    return None
