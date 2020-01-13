from django.shortcuts import render, redirect
def index(request):
    if request.method == "GET":
        print("a GET index request is being made to this route")
        print(request.GET)
    if request.method == "POST":
        print("a POST index request is being made to this route")
        print(request.POST)
        redirect('/some')        
    return render(request, 'new_fourth_django_app/index.html')

def some_function(request):
    if request.method == "GET":
        print("a GET some_function request is being made to this route")
        print(request.GET)
    if request.method == "POST":
        print("a POST some_function request is being made to this route")
        print(request.POST)    
        val_from_field_three = request.POST["three"]
        val_from_field_four = request.POST["four"]
        print(val_from_field_three, val_from_field_four)    
    return redirect('/some')

# def some_function1(request):
#     if request.method == "GET":
#         print("a POST some_function1 request is being made to this route")
#         print(request.POST)
#         val_from_field_three = request.POST["three"]
#         val_from_field_four = request.POST["four"]
#         print(val_from_field_three, val_from_field_four)
#     return redirect('/some')

# def some_function(request):
#     if request.method == "GET":
#     	print("a GET request is being made to this route")
#     	return render(request, "new_fourth_django_app/index.html")
#     if request.method == "POST":
#         print("a POST request is being made to this route")
#     	return redirect("/")

# def some_function1(request):
#     if request.method == "GET":
#     	print(request.GET)
#         return render(request, "new_fourth_django_app/index.html")

#     if request.method == "POST":
#         print(request.POST)
#         return redirect("/")

# def some_function2(request):
#     if request.method == "POST":
#         val_from_field_one = request.POST["one"]
#     	val_from_field_two = request.POST["two"]