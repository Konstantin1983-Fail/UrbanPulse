"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Простая функция для отображения текста на главной странице
def home(request):
    return HttpResponse("Добро пожаловать в проект UrbanDjango!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/', include('task2.urls')),  # Подключаем маршруты task2
    path('task3/', include('task3.urls')),  # Подключаем маршруты task3
    path('task4/', include('task4.urls')),  # Подключаем маршруты task4
    path('task5/', include('task5.urls')),  # Подключаем маршруты task5
    path('', home),  # Добавляем маршрут для корневого URL
]
