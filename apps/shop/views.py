from django.views.generic.list import ListView
from ..monster import models


class ShopListView(ListView):

    model = models.Monster
    template_name = 'shop/shop.html'
    context_object_name = 'monsters'
