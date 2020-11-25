from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, required=True)

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=100, required=True)
    address = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, min_value=8, required=True)