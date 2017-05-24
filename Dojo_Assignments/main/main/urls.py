from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [ # And now we use the include function to pull in our first_app.urls...
      url(r'^', include('apps.uservalidation.urls')),
      url(r'^', include('apps.first_app.urls')),
      url(r'^', include('apps.time_view.urls')),
      url(r'^', include('apps.vinmyMVC.urls'))

  ]
