from django.contrib import admin
from django.urls import path,include
from Browser.views import indexView 

urlpatterns = [
    path('',indexView),
    path('admin/', admin.site.urls),
    path('users/',include("Browser.urls"))
]

