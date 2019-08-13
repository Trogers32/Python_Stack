from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not request.session['counter']:
        request.session['counter'] = 0
    else:
        request.session['counter'] = request.session['counter'] + 1
    request.session['rstring'] = get_random_string(length=14)
    return render(request, 'main/index.html')

def reset(request):
    request.session.clear()
    return redirect('/')