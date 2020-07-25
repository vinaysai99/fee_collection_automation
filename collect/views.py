from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    return render(request,'collect/home.html')

def view_profile(request):
    args={'user':request.user}
    return render(request,'collect/profile.html',args)
