from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, edit_number):
    return HttpResponse(f"placeholder to edit blog: {edit_number}")

def destroy(request, destroy_number):
    return redirect('/')

def red(request):
    return render(request, "first_app/index.html")