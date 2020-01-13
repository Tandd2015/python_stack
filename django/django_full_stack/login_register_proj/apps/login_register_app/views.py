from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
def log_reg_index(request):
    print(request.POST)
    return render(request, "login_register_app/index.html")

def success_index(request):
    if 'users_id' not in request.session or 'users_id' in request.session and request.session['users_id'] == 0:
        return redirect('/')
    else:
        session_user= User.objects.get(id=int(request.session['users_id']))
        context = {
            'userzzz': session_user,
        }
        return render(request, "login_register_app/success.html", context)

def register_submit(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            if len(errors) > 1:
                return redirect('/')
        else:
            new_user = User.objects.create(email_address = request.POST["register_email_input"], password = request.POST["register_password_input"],first_name = request.POST["register_first_name_input"],last_name = request.POST["register_last_name_input"],birthday=request.POST['register_birthday_input'])
            if 'users_id' not in request.session:
                request.session['users_id'] = new_user.id
            else:
                request.session.pop('users_id')
                request.session['users_id']= new_user.id
    return redirect('/success')

def login_submit(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            if len(errors) > 1:
                return redirect('/')
        else:
            new_user = User.objects.filter(email_address=request.POST['login_email_input'])
            for newzzzz in new_user:
                log_user=newzzzz.id
            if 'users_id' not in request.session:
                request.session['users_id'] = log_user
            else:
                request.session.pop('users_id')
                request.session['users_id']= log_user
        return redirect('/success')

def logout(request):
    request.session.pop('users_id')
    request.session['users_id']= 0  
    return redirect('/')