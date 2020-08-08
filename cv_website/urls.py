"""cv_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cv_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_cv/', views.new_cv, name='new_cv'),
    path('select/edit/', views.edit, name='edit'),
    path('bonus/', views.bonus, name='bonus'),
    path('select/', views.select, name='select'),
    path('select/edit/display/', views.tem_display, name='display'),
    path('new_cv/display/', views.new_display, name='display'),
    path('view/', views.view, name='view'),
    path('view/display/', views.view_display, name='display'),
    path('admin/', admin.site.urls),
]
