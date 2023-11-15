from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Monster


class MonsterDetailView(LoginRequiredMixin, DetailView):

    template_name = 'monster/monster_detail.html'
    model = Monster
    context_object_name = 'monster'
    raise_exception = True
