from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('news_home', news_home, name="news_home"),
    path('create_news/', create_news, name="create_news"),
    path('<int:pk>', NewsDetailView.as_view(), name="news_detail"),
    path('<int:pk>/update', NewsUpdateView.as_view(), name="news_update"),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name="news_delete"),
]
