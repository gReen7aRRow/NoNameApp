from django.urls import path
from . import views

urlpatterns = [
     path('monster/<int:pk>/',
         views.MonsterDetailView.as_view(),
         name='monster-detail'
         ),
     path('monster/collect/<int:pk>',
         views.collect_coins,
         name='collect-coins'
         ),
     path('monster/working/<int:pk>',
         views.working,
         name='working'
         ),
]
