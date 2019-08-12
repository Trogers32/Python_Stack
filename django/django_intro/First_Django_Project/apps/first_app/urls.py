from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<edit_number>\d+)/edit$', views.edit),
    url(r'^(?P<destroy_number>\d+)/delete$', views.destroy),
]