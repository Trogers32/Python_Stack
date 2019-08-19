from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.index), #this is your html file redirect
    url(r'^shows/new$', views.add_show),
    url(r'^add_show$', views.add),
    url(r'^shows/(?P<num>\d+)/edit$', views.edit_show),
    url(r'^update/(?P<num>\d+)$', views.update),
    url(r'^shows/(?P<num>\d+)$', views.show_info),
    url(r'^shows/delete/(?P<num>\d+)$', views.delete_show),
    url(r'^purchase$', views.purchase),
    url(r'^thank_you$', views.thanks),
]