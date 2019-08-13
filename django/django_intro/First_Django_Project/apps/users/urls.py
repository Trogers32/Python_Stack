from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^register$', views.register), #this is your html file redirect
    url(r'^login$', views.login),
    url(r'^users$', views.listUsers),
    url(r'^users/new$', views.register),
]