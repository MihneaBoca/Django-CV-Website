from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['first_name'])
    return render(request, 'index.html')


def bonus(request):
    return render(request, 'bonus.html')
