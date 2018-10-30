from django.shortcuts import redirect as dj_redirect
from django.http.response import JsonResponse
from django.conf import settings
from authlib.client import OAuth2Session


def authorize(request):
    return request.oauth.gitlab.authorize_redirect(request, redirect_uri=settings.AUTHLIB_OAUTH_CLIENTS['gitlab']['redirect_uri'])

def redirect(request):
    return JsonResponse(request.oauth.gitlab.authorize_access_token(request))
