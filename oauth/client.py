from authlib.django.client import OAuth
from django.conf import settings


def get_oauth_client(apps):
    oauth_client = OAuth()
    for name, values in apps.items():
        oauth_client.register(name, **values)
    return oauth_client
