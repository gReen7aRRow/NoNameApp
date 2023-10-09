from django.urls import path
from . import views

urlpatterns = [
    path('monster/<int:pk>/', views.MonsterDetailView.as_view(), name='monster-detail'),
]