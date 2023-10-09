from django.views.generic.detail import DetailView
from .models import Monster


class MonsterDetailView(DetailView):

    template_name = 'monster/monster_detail.html'
    model = Monster
    context_object_name = 'monster'
