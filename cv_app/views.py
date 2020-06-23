from django.shortcuts import render
from django.http import HttpResponse
from cv_app.models import CV


# Create your views here.

def index(request):
    if request.method == 'POST':
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        cv = CV.objects.get_or_create(first_name=fn, last_name=ln, email=request.POST['email'],
                                      address=request.POST['address'], phone_number=request.POST['phone_number'],
                                      pers_desc=request.POST['pers_desc'], experience=request.POST['experience'],
                                      education=request.POST['education'], skills=request.POST['skills'],
                                      hobbies=request.POST['hobbies'])[0]
        #return HttpResponse(request.POST['first_name'])
    return render(request, 'index.html')


def bonus(request):
    return render(request, 'bonus.html')
