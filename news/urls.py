from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),  # Маршрут для представления news
    path('platform/news/', views.news, name='news'),  # Маршрут для страницы новостей
]