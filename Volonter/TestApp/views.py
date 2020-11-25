from django.shortcuts import render
from django.http import HttpResponse
from TestApp.models import Events
from TestApp.models import Donate
from TestApp.models import Profile
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
from .forms import RegisterForm
from django.core.mail import send_mail
from .forms import CommentsForm
from django.shortcuts import (HttpResponse, render, redirect, get_object_or_404, reverse, get_list_or_404, Http404)
from django.core.paginator import Paginator


def main_page(request):
    return render(request, 'index.html')


def events_page(request):
    context = dict()
    history = Events.objects.all()
    context['values'] = history
    return render(request, 'Events.html', context)


def event_page(request, pk):
    context = dict()
    print(request)
    history = Events.objects.filter(id=pk)
    context['values'] = history
    return render(request, 'Event.html', context)


@login_required
def book(request):
    if request.method == 'POST':
        print('OK!')


def donate_page(request):
    context = dict()
    history = Donate.objects.all()
    context['values'] = history
    return render(request, 'Donate.html')


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
            for item in history:
                if ((item.email == form.data['email']) and (item.password == form.data['password'])):
                    return HttpResponseRedirect('/Добро пожаловать в личный кабинет/', 'Profile.html')
                else:
                    continue

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'Login.html', {'form': form})


def register_page(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name, email, password, phone, address = form.data['name'], form.data['email'], form.data['password'], \
                                                    form.data['phone'], form.data[
                                                        'address']
            profile = Profile(name=name, email=email, password=password, phone=phone,
                              address=address)
            profile.save()
            return HttpResponseRedirect('/Добро пожаловать в личный кабинет/', 'Profile.html')
        else:
            print(form)

    else:
        form = RegisterForm()
    return render(request, 'Registration.html', {'form': form})


@login_required
def profile_page(request, id):
    user = get_object_or_404(Profile, id=id)
    # if the profile is private and logged in user is not same as the user being viewed,
    # show 404 error
    if user.profile.private and request.user.username != user.username:
        raise Http404

    # if the profile is not private and logged in user is not same as the user being viewed,
    # then only show public snippets of the user
    else:
        name = user.name
        email = user.email
        phone = user.phone
        address = user.address
        user.profile.save()

    snippets = Paginator(request, name, email, phone, address, 5)

    return render(request, '', {'snippets': snippets})


def logout(request):
    auth_logout(request)
    return render(request, 'index.html')


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
