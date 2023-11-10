from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class AccountLoginForm(AuthenticationForm):
    pass


class AccountRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(AccountRegisterForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
