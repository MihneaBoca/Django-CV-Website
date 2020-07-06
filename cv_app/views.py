from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from cv_app.models import CV


# Create your views here.

def index(request):
    if request.method == 'POST':
        # fn = request.POST['first_name']
        # ln = request.POST['last_name']
        cv = CV.objects.get_or_create(username=request.POST['username'], first_name=request.POST['first_name'],
                                      last_name=request.POST['last_name'], email=request.POST['email'],
                                      address=request.POST['address'], phone_number=request.POST['phone_number'],
                                      pers_desc=request.POST['pers_desc'], experience=request.POST['experience'],
                                      education=request.POST['education'], skills=request.POST['skills'],
                                      hobbies=request.POST['hobbies'])[0]
        # return HttpResponse(request.POST['first_name'])
    return render(request, 'index.html')


class DisplayListView(ListView):
    model = CV
    template_name = 'display_list.html'

    def get_queryset(self):
        return CV.objects.all()


def bonus(request):
    return render(request, 'bonus.html')
