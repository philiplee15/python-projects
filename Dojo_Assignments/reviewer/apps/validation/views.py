from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import User

# Create your views here.
def index(request):
    return render(request, 'validation/validate.html')
def login(request):
    verify = User.objects.validate_login(request.POST['username'], request.POST['passy'])
    if 'success' in verify:
        messages.success(request, verify['success'])
        request.session['login'] = True
        request.session['username'] = request.POST['username']
        request.session['id'] = User.objects.get(username=request.POST['username']).id
        return redirect('/dashboard/')
    else:
        messages.error(request, verify['error'])
        return render(request, "validation/validate.html")

def register(request):
    validate = User.objects.validate_registration(request.POST)
    if 'success' in validate:
        messages.success(request, validate['success'])
        return redirect('/')
    else:
        for val in validate['error']:
            messages.error(request, val)
        return redirect('/')
