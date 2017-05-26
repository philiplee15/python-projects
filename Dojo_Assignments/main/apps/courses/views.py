from django.shortcuts import render, HttpResponse, redirect
from .models import CourseName, Description
# Create your views here.
def courses(request):
    context = { "courses": CourseName.objects.all() }
    print(CourseName.objects.name)
    return render(request, 'courses.html', context)
def rendercourse(request):
    name = request.POST['name']
    desc = request.POST['desc']
    course = CourseName.objects.create(name=name)
    description = Description.objects.create(desc=desc)
    description.save()
    return redirect('/')
def remove(request):
    pass
