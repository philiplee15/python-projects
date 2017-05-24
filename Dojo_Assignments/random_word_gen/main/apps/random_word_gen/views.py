from django.shortcuts import render, HttpResponse, redirect
import string
import random
# Create your views here.
def generate(request):
    return render(request, "random_word_gen/word.html")
def randomize(request):
    stringy = ''
    for count in range(1,15):
        stringy+= random.choice(string.ascii_letters)
    request.session['rand'] = stringy
    return redirect('/')
def clear(request):
    print('we cleared')
    request.session['rand'] = ''
    return generate(request)
