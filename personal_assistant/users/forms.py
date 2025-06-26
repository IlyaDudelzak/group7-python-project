from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)

    email = forms.EmailField(required=True)

    password1 = forms.CharField(
        min_length=4, max_length=20, required=True, widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        min_length=4, max_length=20, required=True, widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ["username", "password"]


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={"style": "display: none;"}))

    class Meta:
        model = Profile
        fields = ['avatar']

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        min_length=4, max_length=20, required=True, widget=forms.PasswordInput()
    )
    password1 = forms.CharField(
        min_length=4, max_length=20, required=True, widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        min_length=4, max_length=20, required=True, widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ["old_password", "password1", "password2"]

class ChangeUsernameForm(forms.ModelForm):
    username = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["username"]

class ChangeEmailForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["email"]