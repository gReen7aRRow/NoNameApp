from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile/collect/<int:pk>',
         views.collect_coins,
         name='collect-coins'
         ),
]
