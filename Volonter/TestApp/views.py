from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    #return render(request, 'index.html')
    return HttpResponse(200)