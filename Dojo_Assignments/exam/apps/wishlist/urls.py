from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^dashboard$', views.dashboard, name="dashboard"),
    url(r'^wish_items/(?P<id>\d+)$', views.show_item, name="show_item"),
    url(r'^wish_items/create$', views.create, name="create"),
    url(r'^logout$', views.logout),
    url(r'^add$', views.validate_item),
    url(r'^addtomy$', views.addtomy),
    url(r'^del$', views.delete),
    url(r'^search$', views.search)    
]
