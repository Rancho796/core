from django.urls import path
from . import views as v

urlpatterns =[
    path('usersLogin/',v.browserLogin)
]
