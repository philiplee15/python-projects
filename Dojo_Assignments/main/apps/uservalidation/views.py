from django.shortcuts import render, HttpResponse, redirect
from .models import User


# Create your views here.
def index(request):
    users = User.userManager.all()
    print(users.first_name)
    return render(request, 'login.html')
def login(request):
    username = request.POST['username']
    pw = request.POST['password']
    user = User.userManager.login(username, pw)
    print(type(user))
    if 'error' in user:
        pass
    if 'theuser' in user:
        password
    return HttpResponse("Done running userManager method.")


def register(request):
    return render(request, 'register.html')
def success(request):
    first = request.POST['fname']
    last = request.POST['lname']
    email = request.POST['email']
    username = request.POST['username']
    bday = request.POST['bday']
    pw = request.POST['password']
    newentry = User.userManager.create(first_name=first, last_name=last, email=email,username=username,bday=bday,password=pw)
    return HttpResponse("Done running userManager method.")
