from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect
from ..monster.models import MonsterCounter


class UserProfileView(LoginRequiredMixin, TemplateView):

    template_name = 'personality/profile.html'
    raise_exception = True
    
    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['monsters'] = (MonsterCounter
                .objects
                .filter(owner=self.request.user)
                .select_related('monster')
                .order_by('monster__price')
                )
        
        return context


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