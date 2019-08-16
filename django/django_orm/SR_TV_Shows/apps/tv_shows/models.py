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

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    desc = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Show_validation()