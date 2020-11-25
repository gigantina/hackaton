from django.shortcuts import render
from django.http import HttpResponse
from TestApp.models import Events
from TestApp.models import Donate
from TestApp.models import Users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import LoginForm
from .forms import RegisterForm

def main_page(request):
    return render(request, 'index.html')

def events_page(request):
    context = dict()
    history = Events.objects.all()
    context['values'] = history
    return render(request, 'Events.html', context)

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
            history = Users.objects.all()
            for(item in history):
                if ( (item.email==LoginForm.email) and (item.password==LoginForm.password) ):
                    return HttpResponseRedirect('/Добро пожаловать в личный кабинет/', 'Profile.html')
                    break
                else:
                    continue


    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'Login.html', {'form': form})

def register_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/Добро пожаловать в личный кабинет/', 'Profile.html')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
    return render(request, 'Login.html', {'form': form})