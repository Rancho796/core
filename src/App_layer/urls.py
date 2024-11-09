
from django.contrib import admin
from django.urls import path
from Browser import views as v

urlpatterns = [
    path('',v.indexView),
    path('admin/', admin.site.urls)
]
