from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def main_page_index_template(request):
    return render(request, 'wish_list_app/main_page_index.html')

def register_success_test(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            if len(errors) > 1:
                return redirect('/main')
        else:
            new_user= User.objects.create(name=request.POST['register_name_input'],username=request.POST['register_username_input'],password=request.POST['register_password_input'],hireday=request.POST['register_hireday_input'])
            if 'users_id' not in request.session:
                request.session['users_id'] = new_user.id
            else:
                request.session.pop('users_id')
                request.session['users_id']= new_user.id
        return redirect('/dashboard')

def dashboard_index_template(request):
    if 'users_id' not in request.session or 'users_id' in request.session and request.session['users_id'] == 0:
        return redirect('/main')
    else:
        session_user= User.objects.get(id=int(request.session['users_id']))
        item_list= session_user.users_list_object.all()
        item_list_of_others= Item.objects.exclude(items_list_object=session_user)
        print(item_list_of_others)
        context = {
            'user_in_session': session_user,
            'users_wish_list': item_list,
            'others_wishes': item_list_of_others,
        }
    return render(request, 'wish_list_app/dashboard_page_index.html', context)

def login_success_test(request):
    if request.method == 'POST':
        print('here')
        print(User.objects.all().values())
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            if len(errors) > 1:
                return redirect('/main')
        else:
            new_user = User.objects.filter(username=request.POST['login_username_input'])
            for newzzzz in new_user:
                log_user=newzzzz.id
            if 'users_id' not in request.session:
                request.session['users_id'] = log_user
            else:
                request.session.pop('users_id')
                request.session['users_id']= log_user
        return redirect('/dashboard')

def logout(request):
    request.session.pop('users_id')
    request.session['users_id']= 0  
    return redirect('/main')

def wish_items_index_template(request):
    return render(request, "wish_list_app/wishlist_index.html")

def item_create_success_test(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            if len(errors) > 1:
                return redirect('/wish_items/create')
        else:
            session_user= User.objects.get(id=request.session['users_id'])
            new_item= Item.objects.create(name=request.POST['product_item_input'],items_list_object=session_user)
        return redirect('/dashboard')

def item_delete_success_test(request, the_delete_id):
    new_delete= Item.objects.get(id=the_delete_id)
    new_delete.delete()
    return redirect('/dashboard')

def item_show_index_template(request, the_show_id):
    new_show_item = Item.objects.get(id=the_show_id)
    new_item_list_of_users =User.objects.filter(users_list_object=new_show_item)
    print(new_item_list_of_users)
    context={
        "display_item": new_show_item,
        "user_item_of_add": new_item_list_of_users,
    }
    return render(request, 'wish_list_app/wish_items_display_index.html', context)

def item_add_success(request, the_add_id):
    new_item = Item.objects.get(id=the_add_id)
    new_user = User.objects.get(id=request.session['users_id'])
    new_item1 = Item.objects.create(name=new_item.name, items_list_object=new_user)
    return redirect('/dashboard')