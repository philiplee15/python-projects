from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render(request, "index.html")

def secrets(request):
    thesecret = request.POST['comment']

def register(request):
    return render(request, "register.html")

def validate(request):
    validate = User.objects.validate(request.POST)
    
    return redirect('/')
