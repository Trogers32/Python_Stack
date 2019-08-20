from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import *
import datetime
import bcrypt


def index(request):
    return render(request, "wall/index.html")
    # return redirect(reverse('lr:home'))
