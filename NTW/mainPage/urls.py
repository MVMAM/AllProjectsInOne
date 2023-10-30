from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    path('', mainPage, name="mainPage"),
    path('news/', include('news.urls')),
    path('taskmanager/', include('taskmanager.urls')),
    path('weather/', include('weather.urls')),
]
