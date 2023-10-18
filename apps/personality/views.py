from django.views.generic import TemplateView
from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.models import User
from ..monster.models import Monster, MonsterCounter


"""class ProfileView(TemplateView):

    template_name = 'personality/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = User.objects.all().select_related('profile')
        context['auth_user'] = user_context
        context['summ_array'] = zip(
                                    Monster.objects.order_by('price'),
                                    user_context.values('monster_counter')
                                    )
        return context"""


def user_profile(request):
    user = request.user
    purchases = MonsterCounter.objects.filter(owner=user)
    monsters = Monster.objects.order_by('price')

    monster_data = {}
    for monster in monsters:
        purchased_quantity = purchases.filter(monster=monster).values('quantity')[0]['quantity']
        monster_data[monster] = purchased_quantity if purchased_quantity else 0

    return render(request, 'personality/profile.html', {'user': user, 'monster_data': monster_data})
