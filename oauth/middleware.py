from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.conf import settings

from .client import get_oauth_client


def get_client(request):
    if not hasattr(request, '_cached_oauth'):
        request._cached_oauth = get_oauth_client(settings.AUTHLIB_OAUTH_CLIENTS)
    return request._cached_oauth


class OAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.oauth = SimpleLazyObject(lambda: get_client(request))
