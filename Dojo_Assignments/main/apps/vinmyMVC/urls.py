from django.conf.urls import url
from . import views
urlpatterns = [
      url(r'^ww$', views.index),
      url(r'^users$', views.show)
       # And now we use the include function to pull in our first_app.urls...
  ]
