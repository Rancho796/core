from django.contrib import admin
from django.urls import path,include
from userapp.views import indexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexView),
    path('users',include('userapp.urls'))
]