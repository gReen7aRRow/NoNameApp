from django.views.generic import TemplateView
from django.contrib.auth.models import User
from ..monster.models import Monster


class ProfileView(TemplateView):

    template_name = 'personality/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['auth_user'] = User.objects.all().select_related('profile')
        context['monsters'] = Monster.objects.order_by('price')
        return context
