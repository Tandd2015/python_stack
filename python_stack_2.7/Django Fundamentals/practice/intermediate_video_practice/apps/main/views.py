from django.shortcuts import render, redirect
from django.contrib import messages

#   def index(request):
#     response = "Hello, I am your first request!"
#     return HttpResponse(response)

# Create your views here.
def index(req):
    return render(req, 'main/index.html')

def success(req):
    context = {
        "title":"Success!"
    }
    return render(req, 'main/success.html', context)

def colors(req, color):
    context = {
        "color": color
    }
    return render(req, 'main/colors.html', context)

def process(req):
    # print(req.POST)
    req.session['name'] = req.POST['name']
    # req.session['email'] = req.POST['email']
    # req.session['favorite_language'] = req.POST['favorite_language']
    errors = []

    if len(req.POST['name']) < 2:
        errors.append('Name must be at least 2 characters')

    if len(req.POST['email']) < 5:
        errors.append('Email miust be valid')

    if len(errors) > 1:
        for error in errors:
            messages.error(req, error)
        return redirect('/')
    else: 
        print req.session['name']
    return redirect('/success')