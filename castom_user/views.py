from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView
from castom_user.forms import RegistrationForm, LoginForm

class Registration(CreateView):
    form_class = RegistrationForm
    success_url = '/users/'
    template_name = 'registration.html'

class NewLoginWiew(LoginView):
    form_class = LoginForm
    success_url = '/users/'
    template_name = 'login.html'
    #
    # def get_success_url(self):
    #     return reverse('users:user_list')


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'user_list.html'

    def get_queryset(self):
        return User.objects.all()



