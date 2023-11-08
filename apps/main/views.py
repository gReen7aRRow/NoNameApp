from django.views.generic import TemplateView
from django.shortcuts import render


class IndexView(TemplateView):

    template_name = 'main/index.html'


def page_not_found_view(
        request,
        exception,
        template_name='errors/404.html'):
    
    return render(request,
                  template_name,
                  status=404)