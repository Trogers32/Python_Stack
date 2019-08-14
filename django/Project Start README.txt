django-admin startproject your_project_name_here

django_intro> cd your_project_name_here

your_project_name_here> mkdir apps
// THIS STEP CAN ALSO BE DONE BY MANUALLY CREATING A FILE USING A USER INTERFACE OF SOME KIND, SUCH AS THE FILE CREATION BUTTON IN VSCODE

within app folder
apps> python ../manage.py startapp your_app_name_here

your_app_name_here> touch urls.py

within your_project_name_here/apps/your_app_name_here/urls.py
from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index), #this is your html file redirect
]

within project urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.app_name.urls')),
]

within your_project_name_here/your_project_name_here/settings.py
   INSTALLED_APPS = [
       'apps.your_app_name_here', # added this line. Don't forget the comma!!
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]    # the trailing comma after the last item in a list, tuple, or dictionary is commonly accepted in Python


within your_project_name_here/apps/your_app_name_here/views.py
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')")

python manage.py makemigrations ------used for models
-------makemigrations is a kind of staging. When this command runs, 
Django looks through all our code, finds any changes we made to our models that will affect the database, 
and then formulates the correct Python code to move on to the next step.
-------

ENABLE SESSION python manage.py migrate

your_project_name_here> python manage.py runserver

localhost:8000




SHELL DIRECTIONS
> python manage.py shell
> from apps.book_authors_app.models import *

URL EXAMPLES
urlpatterns = [
    url(r'^$', views.toindex, name='my_index'),
    url(r'^this_app/new$', views.new, name='my_new'),
    url(r'^this_app/(?P<id>\d+)/edit$', views.edit, name='my_edit'),
    url(r'^this_app/(?P<id>\d+)/delete$', views.delete, name='my_delete'),
    url(r'^this_app/(?P<id>\d+)$', views.show, name='my_show'),
]
<!-- Inside your app's index.html file -->
<a href="/target/this_app/new"></a>
<!-- is the equivalent of:  -->
<a href="{% url 'my_new' %}"></a>
<!-- This form's action attribute -->
<form class="" action="/target/this_app/5/delete" method="post">
  <input type="submit" value="Submit">
</form>
<!-- is the equivalent of: -->
<form class="" action="{% url 'my_delete' id=5 %}" method="post">
  <input type="submit" value="Submit">
</form>

REVERSE function
# Inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
# Create your views here.
# Example of an old index method:
def index(request):
    print("hello, I am your first request")
    return redirect('/target/this_app/new')
# Can be transformed to the following:
def index(request):
    print("hello, I am your first request")
    return redirect(reverse('my_new'))
#In a views.py method
return redirect(reverse('users:new'))


NAMESPACE for using multiple apps
urlpatterns = [
    url(r'^accounts/', include('apps.login_reg_app.urls', namespace='users')),
    url(r'^courses/', include('apps.courses_app.urls', namespace='courses')),
]
---reference in template---
<a href="{% url 'courses:index' %}">This link will hit the index route in your courses_app</a>
<a href="{% url 'users:index' %}">And this link will hit the index route in your login_reg_app</a>
