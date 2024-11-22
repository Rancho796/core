from django.urls import path
from .views import v

urlpatterns = [
    path("createUser",v.CreateUser),
]
