from django.shortcuts import render
from django.http import HttpResponse
from TestApp.models import Event
from TestApp.models import Donate
from TestApp.models import Profile
from TestApp.models import Bookings_From_User, CategoryHelp, UuidAndEmail, Achievment, Achievments_From_User
from .mail import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import logout
from .forms import LoginForm
from .forms import EditProfile
from .forms import RegisterForm, CustomPasswordResetForm, CustomUserChangeForm, CustomPasswordChangeForm
from django.core.mail import send_mail
from .forms import CommentsForm
from django.shortcuts import (HttpResponse, render, redirect, get_object_or_404, reverse, get_list_or_404, Http404)
from django.core.paginator import Paginator
from django.contrib.auth import login
from .auth import MyBackend
from notifications.signals import notify
from .Reset import PasswordResetForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib import messages
from .achievments import get_num_events


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = CustomPasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = Profile.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:

                    print('ok')
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_some_mail(email, user.email)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = CustomPasswordResetForm()
    return render(request=request, template_name="password_reset.html",
                  context={"form": password_reset_form})


def main_page(request):
    return render(request, 'index.html')


def events_page(request):
    context = dict()
    history = Event.objects.all()
    context['values'] = history

    return render(request, 'Events.html', context)


def event_page(request, pk):
    context = dict()
    history = Event.objects.filter(id=pk)
    book = Bookings_From_User.objects.filter(user_id=request.user.id, event_id=pk)
    if book:
        status = 'Вы записаны!'
    else:
        status = ''
    context['values'] = history
    context['status'] = status
    return render(request, 'Event.html', context)


@login_required
def book(request, ides):
    ides = str(ides).split(';')
    user_id, event_id = int(ides[0]), int(ides[1])
    user = Profile.objects.get(id=user_id)
    event = Event.objects.get(id=event_id)
    item = Bookings_From_User(event_id=event, user_id=user)
    item.save()
    if get_num_events(user) == 1:
        achieve = Achievments_From_User(user_id=user, achive_id=Achievment.objects.get(id=2))
        achieve.save()

    return redirect('/events')


def achievements_user(request):
    context = dict()
    history = Achievment.objects.all()
    context['open'] = []
    context['closed'] = []
    for achieve in history:
        try:
            user = Profile.objects.get(id=request.user.id)
            a = Achievments_From_User.objects.get(user_id=user, achive_id=achieve)
            if a:
                context['open'].append(achieve)
        except:
            context['closed'].append(achieve)

    return render(request, 'Achieve.html', context)


def donate_page(request, pk):
    context = dict()
    history = Donate.objects.filter(id=pk)
    book = Bookings_From_User.objects.filter(user_id=request.user.id, event_id=pk)
    if book:
        status = 'Вы записаны!'
    else:
        status = ''
    context['values'] = history
    context['status'] = status
    return render(request, 'Donate.html', context)


def event_category(request, pk):
    context = dict()
    history = Event.objects.filter(category_help=CategoryHelp.objects.get(id=pk))
    context['values'] = history
    return render(request, 'Events.html', context)


def donates_page(request):
    context = dict()
    history = Donate.objects.all()
    context['values'] = history

    return render(request, 'Donates.html', context)


def auth(request):
    return redirect('/account')


def get_login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            history = Profile.objects.all()
            email, password = form.data['email'], form.data['password']
            print(email, password)
            back = MyBackend()
            user = back.authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/account/')
            else:
                print('(')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'Login.html', {'form': form})


def about_page(request):
    return render(request, 'About.html')


def register_page(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name, email, phone, address = form.data['name'], form.data['email'], \
                                          form.data['phone'], form.data[
                                              'address']
            password = form.data['password1']
            profile = Profile(name=name, email=email, password=password, phone=phone,
                              address=address, username=email, is_active=0)
            profile.save()
            uu = get_uuid()
            item = UuidAndEmail(uuid=uu, email=email, action=0)
            item.save()
            user = Profile.objects.get(email=email)
            achieve = Achievment.objects.get(id=1)

            achieve_from_user = Achievments_From_User(user_id=user, achive_id=achieve)
            achieve_from_user.save()
            registration(email, name, a=f'https://Ruslan1.pythonanywhere.com/registration/wait/{uu}')
            return HttpResponseRedirect(f'wait/', 'Profile.html')
        else:
            print(form)

    else:
        form = RegisterForm()
    return render(request, 'Registration.html', {'form': form})


def reg_wait(request):
    return render(request, 'Wait.html')


def complete_reg(request, uu):
    try:
        item = UuidAndEmail.objects.get(uuid=uu)
        profile = Profile.objects.get(email=item.email)
        profile.is_active = 1
        profile.save()

        return redirect('https://Ruslan1.pythonanywhere.com/account/')
    except Exception as e:
        return redirect('https://Ruslan1.pythonanywhere.com/')


@login_required
def profile_page(request):
    user = get_object_or_404(Profile, id=request.user.id)
    context = dict()
    context['values'] = user
    if user.is_superuser:
        a = []
        events = Event.objects.filter(owner=user.id)
        for event in events:
            a += Bookings_From_User.objects.filter(event_id=event.id)
    else:
        a = Bookings_From_User.objects.filter(user_id=user)
    context['events'] = a

    return render(request, 'Profile.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/edit/')
        return redirect('/account/edit/')

    else:
        form = EditProfile(instance=request.user)
        args = {'form': form}
        return render(request, 'EditProfile.html', args)


###### CHANGE PASSWORD
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
        else:
            return redirect('/change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, '/change_password', args)
