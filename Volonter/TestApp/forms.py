from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Profile
        fields = ('name', 'email', 'password', 'phone', 'address')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('name', 'email', 'password', 'phone', 'address')


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, required=True)

    email.widget.attrs.update({'class': 'w3-input w3-border', 'required': 'required', 'placeholder': 'Email'})
    password.widget.attrs.update({'class': 'w3-input w3-border', 'required': 'required', 'placeholder': 'Пароль'})


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=100, required=True)
    address = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, min_length=8, required=True)

    name.widget.attrs.update(
        {'class': 'w3-input w3-border', 'required': 'required', 'placeholder': 'ФИО'})
    phone.widget.attrs.update({'class': 'w3-input w3-border', 'required': 'required', 'placeholder': 'Телефон'})
    address.widget.attrs.update(
        {'class': 'w3-input w3-border', 'required': 'required', 'placeholder': 'Адрес регистрации'})
    email.widget.attrs.update({'class': 'w3-input w3-border', 'required': 'required', 'placeholder': 'Email'})
    password.widget.attrs.update({'class': 'w3-input w3-border', 'required': 'required', 'placeholder': 'Пароль'})


class CommentsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    subject = forms.CharField(label='Subject', max_length=100, required=True)
    message = forms.CharField(label='Message', max_length=300, required=True)


class EditProfile(RegisterForm):
    class Meta:
        model = Profile
        fields = ('name', 'email', 'phone', 'address', 'password')
