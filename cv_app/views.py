from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from cv_app.models import CV


# Create your views here.

def index(request):
    if request.method == 'POST':
        # fn = request.POST['first_name']
        # ln = request.POST['last_name']
        if CV.objects.filter(username=request.POST['username']).exists():
            return HttpResponse('Username already exits.')
        cv = CV.objects.get_or_create(username=request.POST['username'], first_name=request.POST['first_name'],
                                      last_name=request.POST['last_name'], email=request.POST['email'],
                                      address=request.POST['address'], phone_number=request.POST['phone_number'],
                                      pers_desc=request.POST['pers_desc'], experience=request.POST['experience'],
                                      education=request.POST['education'], skills=request.POST['skills'],
                                      hobbies=request.POST['hobbies'])[0]
        # return HttpResponse(request.POST['first_name'])
    return render(request, 'index.html')


def edit(request):
    # DisplayElements.as_view()
    data = CV.objects.all()
    if request.method == 'POST':
        # fn = request.POST['first_name']
        # ln = request.POST['last_name']
        CV.objects.filter(username='Adam01').delete()
        cv = CV.objects.get_or_create(username=request.POST['username'], first_name=request.POST['first_name'],
                                      last_name=request.POST['last_name'], email=request.POST['email'],
                                      address=request.POST['address'], phone_number=request.POST['phone_number'],
                                      pers_desc=request.POST['pers_desc'], experience=request.POST['experience'],
                                      education=request.POST['education'], skills=request.POST['skills'],
                                      hobbies=request.POST['hobbies'])[0]
    return render(request, 'edit.html', {'data': data})


class DisplayListView(ListView):
    model = CV
    template_name = 'display_list.html'

    def get_queryset(self):
        return CV.objects.all()

    def edit(self):
        # DisplayElements.as_view()
        if self.method == 'POST':
            # fn = request.POST['first_name']
            # ln = request.POST['last_name']
            cv = CV.objects.get_or_create(username=self.POST['username'], first_name=self.POST['first_name'],
                                          last_name=self.POST['last_name'], email=self.POST['email'],
                                          address=self.POST['address'], phone_number=self.POST['phone_number'],
                                          pers_desc=self.POST['pers_desc'], experience=self.POST['experience'],
                                          education=self.POST['education'], skills=self.POST['skills'],
                                          hobbies=self.POST['hobbies'])[0]
        return render(self, 'edit.html')


class DisplayElements(ListView):
    model = CV
    template_name = 'edit.html'

    def get_queryset(self):
        return CV.objects.all()


def select(request):
    return render(request, 'select.html', )



def bonus(request):
    return render(request, 'bonus.html')

def display(request):
    return render(request, 'display.html')
