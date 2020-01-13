from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.template import loader, Context
import re

# class Blog(object):
#     def __init__(self, blogger_first_name, blogger_last_name, blogger_email_address, blogger_blog):
#         self.blogger_first_name = blogger_first_name # request.POST['first_name']
#         self.blogger_last_name = blogger_last_name # request.POST['last_name']
#         self.blogger_email_address = blogger_email_address # request.POST['email']
#         self.blogger_blog = blogger_blog # request.POST['blogs_text']
        # self.blogs_id = Blog.id
        # Blog.id = len(request.session.blogs) + 1

    # def appender(self):
    #     request.session.blogs.append(self)
    #     return self

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
# Create your views here.

def index(request):
    temp_late = loader.get_template('blogs/index.html')
    rendered = temp_late.render()
    return HttpResponse(rendered)

def new(request):
    new_temp_late = loader.get_template('blogs/new.html')
    new_rendered = new_temp_late.render(request=request)

    return HttpResponse(new_rendered)
    
        

def process(request):
    
    if request.method == 'POST':
        errors = []
        if len(request.POST['first_name']) < 1:
            errors.append('First Name field must not be blank')

        if len(request.POST['last_name']) < 1:
            errors.append('Last Name field must not be blank')
        
        if len(request.POST['email']) < 1:
            errors.append('Email field must not be blank')
        
        if  len(request.POST['email']) > 0 and not EMAIL_REGEX.match(request.POST['email']):
            errors.append('Email address must be a valid email')

        if len(request.POST['blogs_text']) < 1:
            errors.append('Blog field must not be blank')

        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
            return HttpResponseRedirect('/new/')
        return HttpResponseRedirect('/')

        