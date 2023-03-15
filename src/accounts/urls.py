from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login', login_attempt, name='login_attempt'),
    path('register', register, name='register'),
    path('token_send', token_send, name='token_send'),
    path('success', success, name='success'),
    path('verify/<auth_token>' , verify, name='verify'),
    path('error', error, name='error')
]