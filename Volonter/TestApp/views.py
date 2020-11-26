from django.shortcuts import render
from django.http import HttpResponse
from TestApp.models import Event
from TestApp.models import Donate
from TestApp.models import Profile
from TestApp.models import Bookings_From_User, CategoryHelp, UuidAndEmail
from .mail import *

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import LoginForm
from .forms import EditProfile
from .forms import RegisterForm
from django.core.mail import send_mail
from .forms import CommentsForm
from django.shortcuts import (HttpResponse, render, redirect, get_object_or_404, reverse, get_list_or_404, Http404)
from django.core.paginator import Paginator
from django.contrib.auth import login
from .auth import MyBackend
from notifications.signals import notify


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
    ides = str(ides)
    user_id, event_id = int(ides[0]), int(ides[1])
    user = Profile.objects.get(id=user_id)
    event = Event.objects.get(id=event_id)
    item = Bookings_From_User(event_id=event, user_id=user)
    item.save()
    return redirect('/events')


def achievements_user(request):
    user = Profile.objects.get(id=2)
    notify.send(user, recipient=user, verb='you reached level 10')
    return redirect('http://localhost:8000/')


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
            registration('natalyastareeva@gmail.com', email, name, f'http://localhost:8000/registration/wait/{uu}')
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
        return redirect('http://localhost:8000/account/')
    except Exception as e:
        return redirect('http://localhost:8000/')


@login_required
def profile_page(request):
    user = get_object_or_404(Profile, id=request.user.id)
    context = dict()
    context['values'] = user
    print(context['values'])
    # user.profile.save()
    a = Bookings_From_User.objects.filter(user_id=user)
    for i in a:
        print(i)
    context['events'] = a

    return render(request, 'Profile.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/')


@login_required
def comments_page(request):
    if request.method == 'POST':
        f = CommentsForm(request, request.POST)
        if f.is_valid():
            if request.user.is_authenticated:
                name = CommentsForm.cleaned_data['cc_myself']
                email = CommentsForm.cleaned_data['sender']
                subject = CommentsForm.cleaned_data['subject']
                message = CommentsForm.cleaned_data['message']

                recipients = ['nstareeva@gmail.com', 'gigandev@gmail.com']

                send_mail(subject, message, email, recipients)
                return HttpResponseRedirect('/thanks/')
        else:
            return HttpResponseRedirect('/try again/')


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
