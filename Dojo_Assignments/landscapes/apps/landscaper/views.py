from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')
def random(request, img):
    img = int(img)
    pic = ''
    if img > 0 and img < 10:
        pic = 'landscaper/img/1.jpg'
    elif img > 11 and img < 20:
        pic = 'landscaper/img/2,jpg'
    else:
        pic = 'landscaper/img/3.jpg'
    hello = {
        "img":pic
    }
    print(hello)
    return render(request, 'weather.html', hello)
