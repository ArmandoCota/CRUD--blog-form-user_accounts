"""Define URLS patterns for accounts"""

from django.urls import path
from .views import SingUpViwe

urlpatterns = [
    path("signup/", SingUpViwe.as_view(), name='signup'),
]
