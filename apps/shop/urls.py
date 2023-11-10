from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.ShopListView.as_view(), name='shop'),
    path('shop/buy/<int:pk>/', views.buy_monster, name='buy-monster'),
]
