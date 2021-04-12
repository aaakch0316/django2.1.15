from django.urls import path
from . import views

from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token #, obtain_jwt_token

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('token_verifty/', verify_jwt_token),
    path('token_refresh/', refresh_jwt_token),
    path('users/', views.user_list)
]