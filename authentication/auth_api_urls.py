from django.urls import path
from . import auth_api_views

urlpatterns = [

    path(
        'signup/',
        auth_api_views.signup_api
    ),

    path(
        'login/',
        auth_api_views.login_api
    ),

    path(
        'logout/',
        auth_api_views.logout_api
    ),
]