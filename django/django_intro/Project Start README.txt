(djangoPy3Env) > cd python_stack/django/django_intro
(djangoPy3Env) django_intro> django-admin startproject your_project_name_here

(djangoPy3Env) django_intro> cd your_project_name_here
(djangoPy3Env) your_project_name_here> python manage.py runserver

(djangoPy3Env) your_project_name_here> mkdir apps
// THIS STEP CAN ALSO BE DONE BY MANUALLY CREATING A FILE USING A USER INTERFACE OF SOME KIND, SUCH AS THE FILE CREATION BUTTON IN VSCODE

within app folder
(djangoPy3Env) apps> python ../manage.py startapp your_app_name_here

(djangoPy3Env) your_app_name_here> touch urls.py

within your_project_name_here/apps/your_app_name_here/urls.py
from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
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
from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponsecopy("this is the equivalent of @app.route('/'

(djangoPy3Env) your_project_name_here> python manage.py runserver

ENABLE SESSION python manage.py migrate

localhost:8000