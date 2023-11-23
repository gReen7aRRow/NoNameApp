from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
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
