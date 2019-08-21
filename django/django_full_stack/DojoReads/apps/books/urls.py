from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.home),
    url(r'^add_book$', views.add_book),
    url(r'^add/(?P<num>\d+)$', views.add_favorite),
    url(r'^def/(?P<num>\d+)$', views.remove_favorite),
    url(r'^page/add/(?P<num>\d+)$', views.fadd),
    url(r'^(?P<num>\d+)$', views.book_page),
    url(r'^update/(?P<num>\d+)$', views.update),
    url(r'^delete/(?P<num>\d+)$', views.delete),
]