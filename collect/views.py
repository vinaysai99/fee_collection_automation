from django.shortcuts import render
from django.contrib.auth.models import User
from collect.models import *

def home(request):
    return render(request,'collect/home.html')

def view_profile(request):
    args={'user':request.user}
    return render(request,'collect/profile.html',args)

def certificate(request):
    args={'user':request.user}
    return render(request,'collect/certificate.html',args)
