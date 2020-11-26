from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Profile


class MyBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        login_valid = False
        password_valid = False

        for profile in Profile.objects.all():
            if profile.email == email:
                login_valid = True
            if profile.password == password:
                password_valid = True

        if login_valid and password_valid:
            user = Profile.objects.get(email=email)
            return user
        return None

    def get_user(self, user_id):
        try:
            return Profile.objects.get(id=user_id)
        except Profile.DoesNotExist:
            return None
