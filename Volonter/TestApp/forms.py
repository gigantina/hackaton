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


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    password1.widget.attrs.update({'class': 'w3-input w3-border', 'required': 'required', 'placeholder': 'Пароль'})
    password2.widget.attrs.update(
        {'class': 'w3-input w3-border', 'required': 'required', 'placeholder': 'Подтверждение пароля'})

    class Meta:
        model = Profile

        fields = ('name', "email", 'phone', 'address')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'ФИО'}),
            'email': forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Телефон'}),
            'address': forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Адрес'}),
            'password1': forms.TextInput(attrs={'class': 'w3-input w3-border'}),
            'password2': forms.TextInput(attrs={'class': 'w3-input w3-border'})
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        elif password1 and password2 and password1 == password2:
            if len(password1) < 8:
                raise forms.ValidationError('The password must be at least 8 characters long')
            flag = True
            for char in password1:
                if char.isdigit():
                    flag = False
            if flag:
                raise forms.ValidationError('Password must contain at least one digits')

        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CommentsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    subject = forms.CharField(label='Subject', max_length=100, required=True)
    message = forms.CharField(label='Message', max_length=300, required=True)


class EditProfile(RegisterForm, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'email', 'phone', 'address')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'ФИО'}),
            'email': forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Телефон'}),
            'address': forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Адрес'}),
            'password1': forms.TextInput(attrs={'class': 'w3-input w3-border'}),
            'password2': forms.TextInput(attrs={'class': 'w3-input w3-border'})
        }
