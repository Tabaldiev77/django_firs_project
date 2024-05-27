from django.urls import path
from .views import CarViewSet

urlpatterns = [
    path('cars/', CarViewSet.as_view({'get': 'list'}), name='cars')
]
