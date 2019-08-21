from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^home$', views.index),
    url(r'^post$', views.post_message),
    url(r'^post_comment$', views.post_comment),
    url(r'^delete_comment$', views.delete_comment),
    url(r'^delete_message$', views.delete_message),
]