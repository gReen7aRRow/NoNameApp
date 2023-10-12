from django.views.generic.list import ListView
from ..monster.models import Monster


class ShopListView(ListView):

    model = Monster
    template_name = 'shop/shop.html'
    context_object_name = 'monsters'

    def get_queryset(self):
        return Monster.objects.order_by('price')