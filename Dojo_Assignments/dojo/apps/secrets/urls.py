from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^secrets$', views.secrets, name="secret"),
    url(r'^register$', views.register, name="register"),
    url(r'^validate$', views.validate, name="validate")
]
