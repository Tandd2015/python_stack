from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
def log_reg_index(request):
    print(request.POST)
    return render(request, "quote_dash_app/index.html")

def success_index(request):
    if 'users_id' not in request.session or 'users_id' in request.session and request.session['users_id'] == 0:
        return redirect('/')
    else:
        all_quotes = Quote.objects.all()
        session_user= User.objects.get(id=int(request.session['users_id']))
        # one_quote_likes = Like.objects.filter()
        context = {
            'userzzz': session_user,
            'quotezzz': all_quotes,
        }
        return render(request, "quote_dash_app/quotes_index.html", context)

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
    return redirect('/quotes')

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
        return redirect('/quotes')

def logout(request):
    request.session.pop('users_id')
    request.session['users_id']= 0  
    return redirect('/')

def quote_submit(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            if len(errors) > 1:
                return redirect('/quotes')
        else:
            adding = User.objects.get(id=request.session['users_id'])
            new = Quote.objects.create(quote_message=request.POST['quoter_quote_input'], users_quote_id=adding, author_name=request.POST['quoter_author_name_input'])
            new_all_like = new.likes_id
            # print(new_all_like)
    return redirect('/quotes')

def like_submit(request, q_like_id):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            if len(errors) > 1:
                return redirect('/quotes')
        else:
            quote_to_like= Quote.objects.get(id=q_like_id)
            print(quote_to_like.id, quote_to_like.author_name)
            user = User.objects.get(id=quote_to_like.users_quote_id_id)
            if quote_to_like.users_quote_id_id == request.session['users_id']:
                likess=quote_to_like.likes_id.all()
                print(likess[0].id)
                print(likess[0])
                print(likess[0].likers_user_id)
                print(likess[0].likers_quote_id)
                if likess[0].likers_check == False:
                    Like.objects.create(likers_quote_id=quote_to_like, likers_user_id=user, likers_check=True)
                else:
                    print(quote_to_like.users_quote_id_id)
                    print(user.quotes_id.all())
                    print(likess[0].likers_check, " herere")
                    return redirect('/quotes')
            # print(request.session['users_id'])
    return redirect('/quotes')

def edit_user_index(request, the_edit_id):
    user_edit = User.objects.get(id=the_edit_id)
    context= {
        "user_editing": user_edit,
    }
    return render(request, "quote_dash_app/edit_user_index.html", context)

def edit_user_submit(request, the_edit_id):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            if len(errors) > 1:
                return redirect(f'/myaccount/{the_edit_id}')
        else:
            updating= User.objects.get(id=request.session['users_id'])
            updating.email_address= request.POST['edit_email_input']
            updating.password= request.POST['edit_password_input']
            updating.first_name= request.POST['edit_first_name_input']
            updating.last_name= request.POST['edit_last_name_input']
            updating.birthday= request.POST['edit_birthday_input']
            updating.save()
            return redirect('/quotes')
    return redirect(f'/myaccount/{the_edit_id}')

def delete_quote(request, the_delete_id):
    new_delete= Quote.objects.get(id=the_delete_id)
    new_delete.delete()
    return redirect('/quotes')