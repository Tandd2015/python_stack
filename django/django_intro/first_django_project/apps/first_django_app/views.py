from django.shortcuts import render, HttpResponse, redirect
from django import forms
blog_list=['blog1','blog2','blog3','blog4','blog5','blog6']
def index(request):
    new_str=''
    for i in range(len(blog_list)):
        # print(i, blog_list[i])
        if i != len(blog_list)-1:
            new_str+=f'{blog_list[i]}, '
        else:
            new_str+=f'{blog_list[i]}'
    return HttpResponse(new_str)

def new(request):
    form='<form action="" method="POST"><label for="blogged"><h1>Blogs:  </h1><textarea rows="6" cols="40" name="blogged"></textarea><br><button type="submit">Submit Me</button></label></form'
    return HttpResponse(form)

def create(request):
    return redirect('/')

def show(request, number):
    if int(number) <= len(blog_list):
        new_new_str=f'Blog Number : {number} - {blog_list[int(number)-1]}'
        return HttpResponse(new_new_str)
    else:
        return HttpResponse('There are no current blogs by that id number view. Try again please')

def edit(request, number):
    if int(number) <= len(blog_list):
        replace=f'<form action="" method="POST"><label for="replace_blogged"><h1>Replace Blogs Number: {number} </h1><textarea rows="6" cols="40" name="replace_blogged"></textarea><br><button type="submit">Replace Me</button></label></form'
        return HttpResponse(replace)
    else:
        return HttpResponse('There are no current blogs by that id number to edit. Try again please')

def delete(request, number):
    temp=blog_list[int(number)-1]
    if int(number) <= len(blog_list):
        for i in range(int(number)-1, len(blog_list)-1, 1):
            # print (i)
            if i <= len(blog_list):
                blog_list[i], blog_list[i+1] = blog_list[i+1], blog_list[i]
                # print (i, len(blog_list))
        blog_list.pop()
        # print(len(blog_list))
        # print(blog_list)
        last_new_str=f'Blog Number : {number} - {temp}'
        return HttpResponse(last_new_str)
    else:
        return HttpResponse('There are no current blogs by that id number to delete. Try again please')    
