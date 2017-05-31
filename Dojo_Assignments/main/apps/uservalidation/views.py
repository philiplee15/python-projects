from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
import re

# Create your views here.
def index(request):
    users = User.userManager.all()
    print(users)
    return render(request, 'login.html')
    
def login(request):
    username = request.GET['username']
    pw = request.GET['passy']
    user = User.userManager.login(username, pw)
    if 'error' in user:
        messages.error(request, user['error'])
        return redirect('/')
    if 'success' in user:
        return render(request, "forum.html")

def register(request):
    return render(request, 'register.html')
def success(request):
    register = User.userManager.register(request.POST)
    if register['error']:
        for val in register['error']:
            messages.error(request, val)
        return render(request, 'register.html')
    else:
        messages.success(request, register['success'])
        return render(request, 'login.html')
