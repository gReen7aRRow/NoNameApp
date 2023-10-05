from typing import Any
from django.views.generic import TemplateView
from django.contrib.auth.models import User


class ProfileView(TemplateView):

    template_name = 'personality/profile.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['auth_user'] = User.objects.all().select_related('profile')
        return context
