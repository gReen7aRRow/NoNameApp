from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
    path('profile/collect/<int:pk>',
         views.collect_coins,
         name='collect-coins'
         ),
]
