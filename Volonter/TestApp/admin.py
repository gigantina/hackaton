from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Profile
    list_display = ['email', 'name']


admin.site.register(Profile, CustomUserAdmin)
admin.site.register(Event)
admin.site.register(Donate)
admin.site.register(Donates_From_User)
admin.site.register(Bookings_From_User)
admin.site.register(CategoryHelp)
admin.site.register(Achievment)
#admin.site.register(Achievments_From_User)
