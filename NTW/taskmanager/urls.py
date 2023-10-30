from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home_of_taskmanager"),
    path('about', about, name="about"),
    path('create', creator, name="create"),
    path('information', info, name="information"),
    path('<int:pk>', TaskmanagerDetailView.as_view(), name="taskmanager_detail"),
    path('<int:pk>/update', TaskmanagerUpdateView.as_view(), name="taskmanager_update"),
    path('<int:pk>/delete', TaskmanagerDeleteView.as_view(), name="taskmanager_delete"),
]
