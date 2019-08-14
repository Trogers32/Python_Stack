from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context ={
        "books":Book.objects.all()
    }
    return render(request, "main/index.html", context)

def authors(request):
    context = {
        "authors" : Author.objects.all()
    }
    return render(request, "main/authors.html", context)

def book_description(request, num):
    book_desc = {
        'language' : Book.objects.get(id=num).title,
        'ID' : num,
        'desc' : Book.objects.get(id=num).desc,
        'authors' : Book.objects.get(id=num).author.all(),
        'other_auth' : Author.objects.exclude(books=num)
    }
    return render(request, "main/desc.html", book_desc)
    
def author_info(request, num):
    auth_context = {
        'auth' : Author.objects.get(id=num),
        # 'auth_books' : Book.objects.filter(author=num)
    }
    return render(request, "main/author_info.html", auth_context)
    
def add_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')
    
def add_author(request):
    auth_name = request.POST['authors']
    bid = request.POST['hidden']
    auth_name = Author.objects.filter(first_name=auth_name).first()
    Book.objects.get(id=bid).author.add(auth_name)
    return redirect(f'/books/{bid}')
    
def new_author(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')