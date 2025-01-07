from django.urls import path
from .views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('', sign_up_by_html, name='sign_up_by_html'),
    path('django_sign_up/', sign_up_by_django, name='sign_up_by_django'),
]