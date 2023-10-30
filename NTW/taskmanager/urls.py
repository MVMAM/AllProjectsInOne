from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home_of_taskmanager"),
    path('about', views.about, name="about"),
    path('create', views.creator, name="create"),
    path('information', views.info, name="information"),
    path('<int:pk>', views.TaskmanagerDetailView.as_view(), name="taskmanager_detail"),
    path('<int:pk>/update', views.TaskmanagerUpdateView.as_view(), name="taskmanager_update"),
    path('<int:pk>/delete', views.TaskmanagerDeleteView.as_view(), name="taskmanager_delete"),
]
