from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import random
from time import gmtime, strftime

def index(request):
    if 'current_gold' not in request.session:
        request.session['current_gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, "main/index.html")

def process(request):
    hidden_input = request.POST['hidden']
    if hidden_input == 'farm':
        request.session['gold'] = random.randint(10, 20)
        request.session['current_gold'] = int(request.session['current_gold']) + request.session['gold']
        request.session['location'] = 'farm'
        request.session['timer'] = strftime("%A, %B %d, %Y %I:%M %p", gmtime())
        request.session['activities'].append(['positive', f"Earned {request.session['gold']} gold from the {request.session['location']} ({request.session['timer']})"])
    elif hidden_input == 'cave':
        request.session['gold'] = random.randint(5, 10)
        request.session['current_gold'] = int(request.session['current_gold']) + request.session['gold']
        request.session['location'] = hidden_input
        request.session['timer'] = strftime("%A, %B %d, %Y %I:%M %p", gmtime())
        request.session['activities'].append(['positive', f"Earned {request.session['gold']} gold from the {request.session['location']} ({request.session['timer']})"])
    elif hidden_input == 'house':
        request.session['gold'] = random.randint(2, 5)
        request.session['current_gold'] = int(request.session['current_gold']) + request.session['gold']
        request.session['location'] = hidden_input
        request.session['timer'] = strftime("%A, %B %d, %Y %I:%M %p", gmtime())
        request.session['activities'].append(['positive', f"Earned {request.session['gold']} gold from the {request.session['location']} ({request.session['timer']})"])
    elif hidden_input == 'casino':
        request.session['gold'] = random.randint(-50, 50)
        request.session['current_gold'] = int(request.session['current_gold']) + request.session['gold']
        request.session['location'] = hidden_input
        request.session['timer'] = strftime("%A, %B %d, %Y %I:%M %p", gmtime())
        if int(request.session['gold']) < 0:
            request.session['gold'] = int(request.session['gold']) * -1
            request.session['activities'].append(['negative', f"Lost {request.session['gold']} gold from the {request.session['location']} ({request.session['timer']})"])
        else:
            request.session['activities'].append(['positive', f"Earned {request.session['gold']} gold from the {request.session['location']} ({request.session['timer']})"])
    return redirect('/')

def destroy(request):
    request.session.clear()
    return redirect('/')