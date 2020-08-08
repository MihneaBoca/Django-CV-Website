from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from cv_app.models import CV


# Create your views here.

def index(request):
    return render(request, 'index.html')


def new_cv(request):
    return render(request, 'new_cv.html')


def edit(request):
    data = CV.objects.all()
    user_id = request.POST.get('username_select')
    return render(request, 'edit.html', {'data': data, 'user_id': user_id})


def tem_display(request):
    display_data = CV.objects.all()
    display_user_id = request.POST.get('username')
    cv = CV.objects.get(username=display_user_id)
    fn = request.POST.get('first_name')
    cv.first_name = request.POST.get('first_name')
    cv.last_name = request.POST.get('last_name')
    cv.email = request.POST.get('email')
    cv.address = request.POST.get('address')
    cv.phone_number = request.POST.get('phone_number')
    cv.pers_desc = request.POST.get('pers_desc')
    cv.experience = request.POST.get('experience')
    cv.education = request.POST.get('education')
    cv.skills = request.POST.get('skills')
    cv.hobbies = request.POST.get('hobbies')
    cv.save()
    return render(request, 'display.html', {'display_data': display_data, 'display_user_id': display_user_id})


def new_display(request):
    if request.method == 'POST':
        if CV.objects.filter(username=request.POST['username']).exists():
            messages.error(request, "This username already exists.")
            return redirect('new_cv')
        cv = CV.objects.get_or_create(username=request.POST['username'], first_name=request.POST['first_name'],
                                      last_name=request.POST['last_name'], email=request.POST['email'],
                                      address=request.POST['address'], phone_number=request.POST['phone_number'],
                                      pers_desc=request.POST['pers_desc'], experience=request.POST['experience'],
                                      education=request.POST['education'], skills=request.POST['skills'],
                                      hobbies=request.POST['hobbies'])[0]
    display_data = CV.objects.all()
    display_user_id = request.POST.get('username')
    return render(request, 'display.html', {'display_data': display_data, 'display_user_id': display_user_id})


def view_display(request):
    display_data = CV.objects.all()
    display_user_id = request.POST.get('username_select')
    return render(request, 'display.html', {'display_data': display_data, 'display_user_id': display_user_id})


def select(request):
    username = CV.objects.values_list('username', flat=True)
    return render(request, 'select.html', {'username': username})


def view(request):
    username = CV.objects.values_list('username', flat=True)
    data = CV.objects.all()
    return render(request, 'view.html', {'username': username, 'data': data})


def display(request):
    return render(request, 'display.html')
