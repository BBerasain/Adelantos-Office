from django.contrib import admin
from django.urls import path
from miapp.views import login_request, register

urlpatterns = [
    path("login/", login_request, name="login"),
    path("registro/", register, name="registro")
]