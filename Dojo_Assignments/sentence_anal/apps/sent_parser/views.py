from django.shortcuts import render, HttpResponse, redirect
import nltk
from nltk.corpus import treebank
from .pos import pos

# Create your views here.
def index(request):
    return render(request, 'form.html')
def parse(request):
    sentence = request.POST.get('sentence')
    words = nltk.word_tokenize(sentence)
    posdict = pos()
    request.session['dictify'] = dict(nltk.pos_tag(words))
    for key, val in request.session['dictify'].items():
        request.session['dictify'][key] = posdict[val]
    print(request.session['dictify'])
    return redirect('/')
