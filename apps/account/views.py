from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AccountLoginForm, AccountRegisterForm


class LoginUserView(LoginView):

    template_name = 'account/login.html'
    form_class = AccountLoginForm


class RegisterUserView(FormView):

    template_name = 'account/register.html'
    form_class = AccountRegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        
        form.save()

        username = self.request.POST['username']
        password = self.request.POST['password1']

        user = authenticate(username=username, password=password)
        login(self.request, user)

        return redirect(self.success_url)


class LogoutUserView(LogoutView):

    next_page = reverse_lazy('index')
