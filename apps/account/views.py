from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class LoginUserView(TemplateView):

    template_name = 'account/login.html'


class RegisterUserView(TemplateView):

    template_name = 'account/register.html'


class LogoutUserView(LogoutView):

    next_page = reverse_lazy('index')
