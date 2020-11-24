from django.shortcuts import render
from django.http import HttpResponse
from TestApp.models import Events

def main_page(request):
    return render(request, 'index.html')

def events_page(request):
    context = dict()
    history = Events.objects.all()
    context['values'] = history
    return render(request, 'Events.html', context)

def donate_page(request):
    context = dict()
    history = Events.objects.all()
    context['values'] = history
    return render(request, 'Donate.html')