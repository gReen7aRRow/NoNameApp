from django.shortcuts import render
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
