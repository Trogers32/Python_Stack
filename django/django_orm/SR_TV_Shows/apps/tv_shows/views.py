from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import datetime
import bcrypt

######################################
# methods for login and registration
######################################
def home(request):
    return render(request, "main/lr.html")

def success(request):
    try:
        uid = int(request.session['user_id'])
        context = {
            "user" : User.objects.get(id=uid),
        }
        return render(request, "main/success.html", context)
    except:
        return render(request, "main/FAIL.html")

def register(request):
    errors = User.objects.register_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/lr")
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())  # create the hash     
        # make sure you put the hashed password in the database, not the one from the form!
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], bday=request.POST['date'], email=request.POST['email'], password=pw_hash) 
        e = request.POST['email']
        user = User.objects.filter(email=e)
        logged_user = user[0]
        request.session['user_id'] = logged_user.id
    return redirect("/success")

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect("/success")
    return redirect('/lr')
    
def logout(request):
    request.session.clear()
    return redirect("/lr")

###########################################################
def index(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, "main/index.html", context)

def add_show(request):
	return render(request, "main/add_show.html")

def add(request):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
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
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
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
        
def purchase(request):
    if 'total_purchased' not in request.session:
        request.session['total_purchased'] = int(request.POST['amount'])
    else:
        request.session['total_purchased'] += int(request.POST['amount'])
    if 'grand' not in request.session:
        request.session['grand'] = 0
    show_id = Show.objects.get(id=int(request.POST['hidden']))
    request.session['total'] = round(( float(show_id.price) * float(request.POST['amount'])),2)
    request.session['grand'] += request.session['total']
    request.session['grand'] = round(request.session['grand'],2)
    return redirect("/thank_you")

def thanks(request):
    return render(request, "main/purchase.html")

def delete_show(request, num):
    Show.objects.get(id=num).delete()
    return redirect("/shows")

def destroy(request):
    request.session.clear()
    return redirect("/shows")