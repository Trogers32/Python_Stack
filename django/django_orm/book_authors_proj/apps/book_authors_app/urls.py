from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index), #this is your html file redirect
    url(r'^add_book$', views.add_book),
    url(r'^append_book$', views.append_book),
    url(r'^add_author$', views.add_author),
    url(r'^authors$', views.authors),
    url(r'^new_author$', views.new_author),
    url(r'^books/(?P<num>\d+)$', views.book_description),
    url(r'^authors/(?P<num>\d+)$', views.author_info),
]
