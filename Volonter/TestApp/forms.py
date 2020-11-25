from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, required=True)

class RegisterForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    phone = forms.CharField(label='Phone', max_length=100, required=True)
    address = forms.CharField(label='Address', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, min_value=8, required=True)

class CommentsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    subject = forms.CharField(label='Subject', max_length=100, required=True)
    message = forms.CharField(label='Message', max_length=300, required=True)

class EditProfile(RegisterForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'phone', 'address', 'password')

