from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index), #this is your html file redirect
]
