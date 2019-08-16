from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import datetime


def index(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, "main/index.html", context)

def add_show(request):
	return render(request, "main/add_show.html")

def add(request):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/new')
    else:
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], desc=request.POST['desc'], release_date=request.POST['date'])
        num = Show.objects.get(title=request.POST['title']).id
        return redirect(f'/shows/{num}')

def edit_show(request, num):
    new_date = Show.objects.get(id=num).release_date.strftime('%m/%d/%y')
    context = {
        'show' : Show.objects.get(id=num),
        'cdate' : new_date
    }
    return render(request, "main/edit_show.html", context)

def show_info(request, num):
    new_date = Show.objects.get(id=num).release_date.strftime('%B %d, %Y %I:%M %p')
    context = {
        'show' : Show.objects.get(id=num),
        'cdate' : new_date
    }
    return render(request, "main/show_info.html", context)

def update(request, num):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{num}/edit')
    elif request.POST['date'] == "" or request.POST['date'] == '':
        Show.objects.filter(id=num).update(title=request.POST['title'], network=request.POST['network'], desc=request.POST['desc'])
        return redirect("/shows")
    else:
        Show.objects.filter(id=num).update(title=request.POST['title'], network=request.POST['network'], desc=request.POST['desc'], release_date=request.POST['date'])
        return redirect(f"/shows/{num}")

def delete_show(request, num):
    Show.objects.get(id=num).delete()
    return redirect("/shows")
