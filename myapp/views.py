from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    physical = int(request.GET.get('vir'))
    virtual = int(request.GET.get('phy'))
    if request.GET.get('formal'):
        result = physical + virtual
    else:
        result = physical
    
    return render(request, 'generator/password.html', {'score': result})

def about(request):
    return render(request, 'generator/about.html')

