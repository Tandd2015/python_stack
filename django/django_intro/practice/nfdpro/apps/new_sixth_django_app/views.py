# Still inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
# from django.core.urlresolvers import reverse
# Create your views here.
# Example of an old index method:
def index(request):
    print('just hello')
    return render(request, 'new_sixth_django_app/index.html')
# def new(request):
#     print("hello, I am your second request")
#     return redirect(reverse('index'))
def toindex(request):
    print("hello, I am your first request")
    return redirect('/six/')
    # return redirect(reverse('index'))
# Can be transformed to the following:
#In a views.py method
#In a views.py method
# return redirect(reverse('users:new'))
# return redirect(reverse('users:show', kwargs={'id': your_id_variable }))