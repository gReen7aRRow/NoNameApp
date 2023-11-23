from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Monster, MonsterCounter
from .tasks import working_task


class MonsterDetailView(LoginRequiredMixin, DetailView):

    template_name = 'monster/monster_detail.html'
    model = Monster
    context_object_name = 'monster'
    raise_exception = True


def collect_coins(request, pk):
    user = request.user
    monster = (MonsterCounter
              .objects
              .get(owner=user, monster=pk)
              )
    
    user.profile.balance += monster.wealth
    monster.wealth = 0

    user.save()
    monster.save()
    
    return redirect('profile')


def working(request, pk):
    user = request.user
    monster = (MonsterCounter
               .objects
               .select_related('monster')
               .get(owner=user, monster=pk)
              )

    if monster.wealth < monster.monster.productivity * monster.quantity * 10:

        working_task.delay()

        monster.wealth += monster.monster.productivity
        monster.save()

        return redirect('profile')
    
    else:
        return redirect('shop')
