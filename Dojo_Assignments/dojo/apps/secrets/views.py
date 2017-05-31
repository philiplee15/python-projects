from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Secret, Like
from django.db.models import Count

# Create your views here.
def index(request, sort):
    print(sort)
    if 'login' not in request.session:
        request.session['login'] = False
    if sort == 'popular':
        pass
    elif sort == 'new':
        pass
    else:
        allsecrets = Secret.objects.all().annotate(Count("secret_like")).order_by("-id")
    context = {
        "list": allsecrets
    }
    return render(request, "index.html", context)

def run_secrets(request):
    if request.session['login'] == True:
        secretlist = Secret.objects.validate_secret(request.POST, request.session['id'])
    else:
        messages.error(request, "You must login to post.")
        return redirect('/')
    if 'error' in secretlist:
        messages.error(request, secretlist['error'])
        return redirect('/')
    else:
        messages.success(request, secretlist['success'])
        print(secretlist)
        return redirect('/')

def register(request):
    return render(request, "register.html")

def validate(request):
    validate = User.objects.validate(request.POST)
    if 'success' in validate:
        messages.success(request, validate['success'])
        return render(request, 'index.html')
    else:
        for val in validate['error']:
            messages.error(request, val)
        return render(request, 'register.html')

def verify(request):
    verify = User.objects.verify(request.POST)
    if 'success' in verify:
        messages.success(request, verify['success'])
        request.session['login'] = True
        request.session['username'] = request.POST['user']
        request.session['id'] = User.objects.get(username=request.POST['user']).id
        return redirect('/')
    else:
        messages.error(request, verify['error'])
        return redirect('/')

def logout(request):
    del request.session['login']
    del request.session['username']
    del request.session['id']
    request.session.modified = True
    return redirect('/')
def like(request):
    print(request.POST)
    if 'delete' in request.POST:
        secret = Secret.objects.get(id=request.POST['delete']).delete()
        return redirect('/')
    if 'like' in request.POST:
        try:
            secret = Secret.objects.get(id=request.POST['like'])
            user = User.objects.get(id=request.session['id'])
            like = Like.objects.create(secret=secret, user=user)
            return redirect('/')
        except:
            messages.error(request, "Not logged in.")
            return redirect('/')
