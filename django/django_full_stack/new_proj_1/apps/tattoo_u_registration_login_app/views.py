from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import *

#--- Registration Page Functions
def registration_index_page_load(request):
    return render(request, 'tattoo_u_registration_login_app/registration_index_template.html')

def registration_form_submit(request):
    return redirect('/registration')

#--- Login Page Functions
def login_index_page_load(request):
    return render(request, 'tattoo_u_registration_login_app/login_index_template.html')

def login_form_submit(request):
    return redirect('/login')

#--- User Dashboard Page Functions
def user_dashboard_index_page_load(request):
    return render(request, 'tattoo_u_registration_login_app/session_user_index_template.html')

def user_dashboard_form_submit(request):
    return redirect('/dashboard')


#--- Nav Bar Redirect Function
def registration_redirect(request):
    return redirect('/registration')

def login_redirect(request):
    return redirect('/login')

def logout_redirect(request):
    return redirect('/login')