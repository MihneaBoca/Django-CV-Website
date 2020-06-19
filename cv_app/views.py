from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def bonus(request):
    return render(request, 'bonus.html')