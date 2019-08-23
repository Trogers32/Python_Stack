from django.shortcuts import render, redirect
from django.contrib import messages
from apps.login_registration.models import *
import datetime
import bcrypt
from django.core.urlresolvers import reverse

def home(request):
    return render(request, "belt/index.html")