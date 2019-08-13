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
    return HttpResponsecopy("this is the equivalent of @app.route('/')")

ENABLE SESSION python manage.py migrate

your_project_name_here> python manage.py runserver

localhost:8000