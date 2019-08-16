from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows$', views.index), #this is your html file redirect
    url(r'^shows/new$', views.add_show),
    url(r'^shows/(?P<num>\d+)/edit$', views.edit_show),
    url(r'^shows/(?P<num>\d+)$', views.show_info),
]