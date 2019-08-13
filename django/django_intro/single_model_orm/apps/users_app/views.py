from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')")