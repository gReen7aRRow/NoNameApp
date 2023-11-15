from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..monster.models import Monster, MonsterCounter
from django.shortcuts import get_object_or_404, redirect


class ShopListView(LoginRequiredMixin, ListView):

    model = Monster
    template_name = 'shop/shop.html'
    context_object_name = 'monsters'
    raise_exception = True

    def get_queryset(self):
        return Monster.objects.order_by('price')


def buy_monster(request, pk):
    monster = get_object_or_404(Monster, pk=pk)
    quantity = int(request.POST['quantity'])
    summ = monster.price * quantity

    if request.user.profile.balance >= summ:
        counter = MonsterCounter.objects.get(owner=request.user, monster=pk)

        request.user.profile.balance -= summ
        counter.quantity += quantity

        request.user.save()
        counter.save()

        return redirect('profile')

    else:
        return redirect('shop')
