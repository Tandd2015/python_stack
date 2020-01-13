from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    if request.method == "GET": 
        print('get')
    
    if 'ran_str' not in request.session:
        request.session['ran_str']= get_random_string(length=14)
        print('hello new ran str')
    else:
        del request.session['ran_str']
        request.session['ran_str']= get_random_string(length=14)
        print('stage 2')

    if 'counter' not in request.session:
        request.session['counter']=1
    else:
        request.session['counter']+=1

    if 'ran_str' in request.session and 'counter' in request.session:
        context = {
            'ran_str': request.session['ran_str'],
            'counter': request.session['counter'],
        }
    return render(request, 'first_django_app/index.html', context)

def function_one(request):
    if request.method == 'POST':
        del request.session['ran_str']
        print('hello world')
    return redirect('/random_word')

def function_two(request):
    del request.session['counter']
    print('here too')
    return redirect('/random_word')