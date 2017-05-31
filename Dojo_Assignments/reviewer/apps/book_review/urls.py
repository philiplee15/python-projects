from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^dashboard/add$', views.add, name="add"),
    url(r'^dashboard/(?P<id>\d+)$', views.show_book, name="show_book"),
    url(r'^dashboard/users/(?P<id>\d+)$', views.show_user, name=""),
    url(r'^submitbook$', views.submitbook),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^delete$', views.delete, name="delete"),
    url(r'^search$', views.search, name="search")
]
