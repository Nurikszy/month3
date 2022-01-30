from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models

ADMIN = 1
VIPCLIENT = 2
KLIENT = 3
user_type = (
    (ADMIN, 'ADMIN'),
    (VIPCLIENT, 'VIPCLIENT'),
    (KLIENT, 'CLIENT'),
)
MALE = 1
FEMALE = 2
OTHER = 3
gender_type = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE'),
    (OTHER, 'OTHER'),
)
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=gender_type, required=True)
    user_type = forms.ChoiceField(choices=user_type,required=True)
    class Meta:
        model = models.CastomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "user_type",
            "gender"
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)


    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'username', 'id': 'hello'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": 'form_control',
            "placeholder": 'password',
            "id": 'hi',
        }
    ))
