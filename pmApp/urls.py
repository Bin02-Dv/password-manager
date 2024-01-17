from django.urls import path
from .views import password_manager, add_password

urlpatterns = [
    path('', password_manager, name='password_manager'),
    path('add_password/', add_password, name='add_password'),
]