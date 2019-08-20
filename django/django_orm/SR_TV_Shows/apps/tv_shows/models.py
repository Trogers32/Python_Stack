from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class Show_validation(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["name"] = "Title should be at least 5 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors["desc"] = "Description should be at least 10 characters"
        if postData['date'] == '':
            i=1
        elif datetime.strptime(postData['date'], '%Y-%m-%d') >= datetime.today():
            errors["date"] = "Date should be in the past."
        if Show.objects.filter(title=postData['title']).first():
            errors["dupe"] = "Can't be a duplicate title."
        return errors

    def add_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["name"] = "Title should be at least 5 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors["desc"] = "Description should be at least 10 characters"
        if postData['date'] >= datetime.today():
            errors["date"] = "Date should be in the past."
        if postData['date'] == "":
            errors["date"] = "Date can't be empty."
        if Show.objects.filter(title=postData['title']).first():
            errors["dupe"] = "Can't be a duplicate title."
        return errors

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
        else:
            today = datetime.now().year
            bday = datetime.strptime(postData['date'], '%Y-%m-%d')
            bday = bday.year - today
            if bday < 13:
                errors["date"] = "You have to be older than 13 to join this site."
        if User.objects.filter(email=postData['email']).first():
            errors["email"] = "Email already registered."
        if len(postData['password']) < 8:
            errors["password"] = "Password needs to be at least 8 characters long."
        elif postData['password'] != postData['confirm_password']:
            errors["password"] = "Passwords do not match."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    desc = models.TextField()
    release_date = models.DateField()
    price = models.DecimalField(max_digits=999, decimal_places=2, default=19.99)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Show_validation()

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bday = models.DateField()
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = User_validation()