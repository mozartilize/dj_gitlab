from django.urls import path, include
from . import views

app_name = 'oauth'

urlpatterns = [
    path('oauth/', include([
        path('redirect/', views.redirect, name='redirect'),
        path('authorize/', views.authorize, name='authorize'),
    ]))
]
