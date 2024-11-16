from django.contrib import admin
from django.urls import path
from userapp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.indexView),
    path('user/create-user/',v.createUser)
]