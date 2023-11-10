from django.shortcuts import render, redirect
from ..monster.models import MonsterCounter


def user_profile(request):
    monsters = (MonsterCounter
                .objects
                .filter(owner=request.user)
                .select_related('monster')
                .order_by('monster__price')
                )

    context = {
        'monsters': monsters,
    }

    return render(request, 'personality/profile.html', context=context)

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