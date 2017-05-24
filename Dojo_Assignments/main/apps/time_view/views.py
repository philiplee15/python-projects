from django.shortcuts import render, HttpResponse
import datetime
#CONTROLLER
# Create your views here.
def time(request):
    test = {
    "time": datetime.datetime.now().time(),
    "date": datetime.datetime.now().date()
    }
    return render(request, "time_view/index.html", test)
