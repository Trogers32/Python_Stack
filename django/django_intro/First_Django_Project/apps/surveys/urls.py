from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^surveys$', views.index), #this is your html file redirect
    url(r'^surveys/new$', views.new),
]