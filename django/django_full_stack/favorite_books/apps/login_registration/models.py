from __future__ import unicode_literals
from django.db import models
from datetime import datetime, timedelta
import bcrypt
import pytz


class User_validation(models.Manager):   
    def register_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["fname"] = "First name should be at least 2 characters long."
        if len(postData['last_name']) < 3:
            errors["lname"] = "Last name should be at least 2 characters long."
        if datetime.strptime(postData['date'], '%Y-%m-%d') >= datetime.today():
            errors["date"] = "Birthday should be in the past."
        elif postData['date'] == "":
            errors["date"] = "Birthday can't be empty."
        # else:
        #     today = datetime.now().year
        #     bday = datetime.strptime(postData['date'], '%Y-%m-%d')
        #     bday = bday.year - today
        #     if bday < 13:
        #         errors["date"] = "You have to be older than 13 to join this site."
        if User.objects.filter(email=postData['email']).first():
            errors["email"] = "Email already registered."
        if len(postData['password']) < 8:
            errors["password"] = "Password needs to be at least 8 characters long."
        elif postData['password'] != postData['confirm_password']:
            errors["password"] = "Passwords do not match."
        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if user:
            logged_user = user[0] 
            if not bcrypt.checkpw(postData['password'].encode(), logged_user.password.encode()):
                errors['pword'] = "Incorrect email or password."
        else:
            errors['pword'] = "Incorrect email or password."
        return errors

class Delete_validation(models.Manager): 
    def delete_validator(self, postData):
        errors = {}  
        cid = int(postData['del_comm'])
        check = Comment.objects.get(id=cid)
        utc=pytz.UTC
        tc = check.created_at
        ct = datetime.utcnow()
        tc = tc.replace(tzinfo=None)
        tc = ct-tc
        tc = tc.seconds / 60
        if tc > 30:
            errors["date"] = "Messages and comments cannot be deleted after 30 minutes."
        return errors

    def delete_mess_validator(self, postData):
        errors = {}  
        cid = int(postData['del_mess'])
        check = Message.objects.get(id=cid)
        utc=pytz.UTC
        tc = check.created_at
        ct = datetime.utcnow()
        tc = tc.replace(tzinfo=None)
        tc = ct-tc
        tc = tc.seconds / 60
        if tc > 30:
            errors["date"] = "Messages and comments cannot be deleted after 30 minutes."
        return errors

class Book_validation(models.Manager):   
    def book_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['description']) < 5:
            errors["desc"] = "Description needs at least 5 characters."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bday = models.DateField()
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = User_validation()

class Book(models.Model):
    uploaded_by = models.ForeignKey(User, related_name="book")
    title = models.CharField(max_length=255)
    desc = models.TextField()
    favorites = models.ManyToManyField(User, related_name="favorite_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Book_validation()

