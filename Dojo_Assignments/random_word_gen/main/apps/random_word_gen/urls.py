from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.generate),
    url(r'^generate$', views.randomize),
    url(r'^clear$', views.clear)
    ]
