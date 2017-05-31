from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^secrets$', views.run_secrets, name="secret"),
    url(r'^register$', views.register, name="register"),
    url(r'^validate$', views.validate, name="validate"),
    url(r'^verify$', views.verify, name="verify"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^like$', views.like, name="like"),
    url(r'^(?P<sort>\w*?)$', views.index, name="index")
]
