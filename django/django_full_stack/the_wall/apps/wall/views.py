from django.shortcuts import render, redirect
from django.contrib import messages
from apps.login_registration.models import *
from datetime import datetime, timedelta
import bcrypt
import pytz


def index(request):
    try:
        uid = request.session['user_id']
        context = {
            "pmessages" : Message.objects.all(),
            "comments" : Comment.objects.all(),
            "user" : User.objects.get(id=uid),
        }
        return render(request, "wall/index.html", context)
    except:
        return redirect("/") 

def post_message(request):
    uid = int(request.POST['user'])
    uid = User.objects.get(id=uid)
    Message.objects.create(user=uid, message=request.POST['message_text'])
    return redirect("/wall")

def post_comment(request):
    uid = int(request.POST['user'])
    uid = User.objects.get(id=uid)
    mid = int(request.POST['mess'])
    mid = Message.objects.get(id=mid)
    Comment.objects.create(user=uid, message=mid, comment=request.POST['comment_text'])
    return redirect("/wall")

def delete_comment(request):
    errors = Comment.objects.delete_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/wall")
    else:
        cid = int(request.POST['del_comm'])
        check = Comment.objects.get(id=cid)
        if(check.user.id == int(request.session['user_id'])):
            Comment.objects.get(id=cid).delete()
    return redirect("/wall")

def delete_message(request):
    errors = Message.objects.delete_mess_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/wall")
    else:
        mid = int(request.POST['del_mess'])
        check = Message.objects.get(id=mid)
        if(check.user.id == int(request.session['user_id'])):
            Message.objects.get(id=mid).delete()
    return redirect("/wall")