from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import datetime

# Create your views here.
def index1(request):
    return render(request, 'show_maker/index.html')

def new_show_add(request):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            if len(errors) > 1:
                return redirect('/shows/new')
            elif len(errors) == 1 and "description_input" not in errors:
                return redirect('/shows/new')
            elif len(errors) == 1 and "description_input" in errors:
                new_show_added= Show.objects.create(title=request.POST['add_title_input'],network=request.POST['add_network_input'],descript="None was not given!", rel_date=request.POST['add_release_date_input'])
                return redirect(f'/shows/{new_show_added.id}')
        else:
            new_show_added= Show.objects.create(title=request.POST['add_title_input'],network=request.POST['add_network_input'],descript=request.POST['add_description_input'], rel_date=request.POST['add_release_date_input'])
            return redirect(f'/shows/{new_show_added.id}')

def new_show_index(request, the_show_id):
    showing= Show.objects.get(id=the_show_id)
    context= {
        'watching': showing,
    }
    return render(request, 'show_maker/new_show_index.html', context)

def all_show_index(request):
    all_shows = Show.objects.all()
    context = {
        'showzzz': all_shows,
    }
    return render(request, 'show_maker/all_show_index.html', context)

def edit_show_index(request, the_edit_id):
    edit_shows= Show.objects.get(id=the_edit_id)
    context= {
        'editzzz': edit_shows,
    }
    return render(request, 'show_maker/edit_show_index.html', context)

def update_show(request, the_update_id):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            if len(errors) > 1:
                return redirect(f'/shows/{the_update_id}/edit')
            elif len(errors) == 1 and "edit_description_input" not in errors:
                return redirect(f'/shows/{the_update_id}/edit')
            elif len(errors) == 1 and "edit_description_input" in errors:
                updating= Show.objects.get(id=the_update_id)
                updating.title= request.POST['edit_title_input']
                updating.network= request.POST['edit_network_input']
                updating.rel_date= request.POST['edit_release_date_input']
                updating.descript= request.POST['edit_description_input']
                updating.save()
                return redirect(f'/shows/{the_update_id}')
        else:
            updating= Show.objects.get(id=the_update_id)
            updating.title= request.POST['edit_title_input']
            updating.network= request.POST['edit_network_input']
            updating.rel_date= request.POST['edit_release_date_input']
            updating.descript= request.POST['edit_description_input']
            updating.save()
            return redirect(f'/shows/{the_update_id}')
    return redirect(f'/shows/{the_update_id}/edit')

def destroy_show(request, the_destroy_id):
    destroyed= Show.objects.get(id=the_destroy_id)
    destroyed.delete()
    return redirect('/shows')