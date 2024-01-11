from django.urls import path
from .views import attack_view

urlpatterns = [
    path('attack/<str:password>/', attack_view),
]
