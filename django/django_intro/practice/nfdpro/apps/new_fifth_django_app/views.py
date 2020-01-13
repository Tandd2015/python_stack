from django.shortcuts import render, redirect
def index(request):
    if request.method == "GET":
        print("a GET index request is being made to this route")
        print(request.GET)
    if request.method == "POST":
        print("a POST index request is being made to this route")
        print(request.POST)
        redirect('/session')        
    return render(request, 'new_fifth_django_app/index.html')

def some_function(request):
    if request.method == "GET":
        print("a GET some_function request is being made to this route")
        print(request.GET)
    if request.method == "POST":
        print("a POST some_function request is being made to this route")
        print(request.POST)    
        val_from_field_three = request.POST["name"]
        val_from_field_four = request.POST["counter"]
        request.session['name'] = request.POST['name']
        request.session['counter'] = request.POST['counter']
        print(val_from_field_three, val_from_field_four, request.session['name'], request.session['counter'])    
    return redirect('/session')

# def some_function1(request):
#     if request.method == "GET":
#         print("a POST some_function1 request is being made to this route")
#         print(request.POST)
#         val_from_field_three = request.POST["three"]
#         val_from_field_four = request.POST["four"]
#         print("another one", val_from_field_three, "another one", val_from_field_four)
#     return redirect('/session')
