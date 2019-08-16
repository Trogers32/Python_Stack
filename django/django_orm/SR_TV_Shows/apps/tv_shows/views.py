from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q, Count

def index(request):
	return render(request, "main/index.html")

def add_show(request):
	return render(request, "main/add_show.html")

def edit_show(request):
	return render(request, "main/edit_show.html")

def show_info(request):
	return render(request, "main/show_info.html")
