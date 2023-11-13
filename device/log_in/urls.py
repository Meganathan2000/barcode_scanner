from django.urls import path
from .views import register

urlpatterns = [
    # Other URL patterns
    path('register/', register, name='register'),
    
]