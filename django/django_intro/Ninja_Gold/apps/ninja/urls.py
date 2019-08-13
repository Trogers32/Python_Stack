from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index), #this is your html file redirect
    url(r'^process_money$', views.process),
    url(r'^destroy_session$', views.destroy),
]