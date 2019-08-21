from django.shortcuts import render, redirect
from django.contrib import messages
from apps.login_registration.models import *
import datetime
import bcrypt
from django.core.urlresolvers import reverse

def home(request):
    try:
        uid = int(request.session['user_id'])
        context = {
            "user" : User.objects.get(id=uid),
            "books" : Book.objects.all(),
            "fav" : Book.objects.filter(favorites=uid),
        }
        return render(request, "books/index.html", context)
    except:
        return redirect("/")

def add_book(request):
    try:
        errors = Book.objects.book_validator(request.POST)
            # check if the errors dictionary has anything in it
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/books")
        else:
            uid = int(request.session['user_id'])
            title = request.POST['title']
            desc = request.POST['description']
            user = int(request.session['user_id'])
            user = User.objects.get(id=user)
            Book.objects.create(uploaded_by=user, title=request.POST['title'], desc=request.POST['description'])
            fav_book = Book.objects.get(title=request.POST['title'])
            user.favorite_books.add(fav_book)
            return redirect('/books')
    except:
        redirect('/login')

def add_favorite(request, num):
    try:
        uid = int(request.session['user_id'])
        book = Book.objects.get(id=num)
        user = User.objects.get(id=uid)
        user.favorite_books.add(book)
        return redirect('/books')
    except:
        return redirect('/login')

def book_page(request, num):
# try:
    uid = int(request.session['user_id'])
    context = {
        "user" : User.objects.get(id=uid),
        "book" : Book.objects.get(id=num),
    }
    return render(request, 'books/desc.html', context)
# except:
    return redirect('/login')

def update(request, num):
    try:
        errors = Book.objects.book_validator(request.POST)
            # check if the errors dictionary has anything in it
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/books/{num}")
        else:
            uid = int(request.session['user_id'])
            Book.objects.filter(id=num).update(title=request.POST['title'], desc=request.POST['description'])
            return redirect(f"/books/{num}")
    except:
        return redirect('/login')

def delete(request, num):
# try:
    uid = int(request.session['user_id'])
    Book.objects.get(id=num).delete()
    return redirect("/books")
# except:
    return redirect('/login')

def fadd(request, num):
    try:
        uid = int(request.session['user_id'])
        book = Book.objects.get(id=num)
        user = User.objects.get(id=uid)
        user.favorite_books.add(book)
        return redirect(f'/books/{num}')
    except:
        return redirect('/login')

def remove_favorite(request, num):
# try:
    uid = int(request.session['user_id'])
    book = Book.objects.get(id=num)
    User.objects.get(id=uid).favorite_books.remove(book)
    return redirect(f"/books/{num}")
# except:
    return redirect('/login')