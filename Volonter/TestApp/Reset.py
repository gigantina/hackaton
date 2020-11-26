
from django.contrib.auth.forms import PasswordResetForm as DjangoPasswordResetForm
from django.core.exceptions import ValidationError
from rest_auth.serializers import (
    PasswordResetSerializer as RestAuthPasswordResetSerializer
)
from rest_auth.views import PasswordResetView as RestAuthPasswordResetView


class PasswordResetForm(DjangoPasswordResetForm):
    def get_users(self, email):
        users = tuple(super().get_users(email))
        email.widget.attrs.update({'class': 'w3-input w3-border', 'required': 'required', 'placeholder': 'Email'})
        if users:
            return users
        msg = f'"{email}" was not found in our system.'
        raise ValidationError(msg)


class PasswordResetSerializer(RestAuthPasswordResetSerializer):
    password_reset_form_class = PasswordResetForm


class PasswordResetView(RestAuthPasswordResetView):
    serializer_class = PasswordResetSerializer
