from django.shortcuts import render, HttpResponse, redirect, session
import datetime

def index(request):
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render(request, 'random_word/index.html')

def reset(request):
    session.clear()
    return redirect('/')