from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib import messages
from django.template import loader, Context, RequestContext
import re
import datetime
from operator import attrgetter
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
import json

class Blog(object):
    blog_id = 0
    def __init__(self, blogger_first_name, blogger_last_name, blogger_email_address, blogger_blog):
        self.blogger_first_name = blogger_first_name # request.POST['first_name']
        self.blogger_last_name = blogger_last_name # request.POST['last_name']
        self.blogger_email_address = blogger_email_address # request.POST['email']
        self.blogger_blog = blogger_blog # request.POST['blogs_text']
        self.time_of_blog = datetime.datetime.now()
        self.blogs_id = Blog.blog_id

        Blog.blog_id += 1
        
    def display_blog(self):
        for attribute, value in self.__dict__.iteritems():
            ammended_attribute = attribute.replace("_", " ")
            if attribute == "time_of_blog":
                print ammended_attribute + ":  " + value.strftime("%I:%M %p")
            else:
                print ammended_attribute + ":  " + str(value) 
        return self

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
# Create your views here.

def index(request):
    temp_late = loader.get_template('blogs/index.html')
    rendered = temp_late.render(request=request)
    return HttpResponse(rendered)

def new(request):
    new_temp_late = loader.get_template('blogs/new.html')
    new_rendered = new_temp_late.render(request=request)
    
    if request.method == 'POST':

            # class LazyEncoder(DjangoJSONEncoder):
            #         def default(self, object):
            #             if isinstance(object, self):
            #                 return str(object)
            #             return super().default(object)
            # serialize('json', self.objects.all(), cls=LazyEncoder)
        class Blogs(Blog):
            def __init__(self, blogger_first_name = request.POST['first_name'], blogger_last_name = request.POST['last_name'], blogger_email_address = request.POST['email'], blogger_blog = request.POST['blogs_text']):
                self.blogs_holder = []
                self.que_size  = self.blogs_holder_counter()
                super(Blogs, self).__init__(blogger_first_name, blogger_last_name, blogger_email_address, blogger_blog)
        
            def blogs_holder_counter(self):
                return len(self.blogs_holder)

            def blogs_appender(self):
                Blogs.n_blog = self
                self.blogs_holder.append(Blogs.n_blog)
                return self

            def display_blogs_holder(self):
                for index in range(len(self.blogs_holder)):
                    for attribute, value in self.blogs_holder[index].__dict__.iteritems():
                        attribute_rename = attribute.replace("_", " ")
                        if attribute == "time_of_blog":
                            display_time = attribute_rename + ":  " + value.strftime("%I:%M %p")
                            print display_time
                        else:
                            print attribute_rename + ":  " + str(value)
                return self

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
            return redirect('/new')
        else:
            Blogs().blogs_appender().display_blogs_holder()
            # if 'new_blog' not in request.session:
            #     request.session['new_blog'] = Blog(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['blogs_text'])
            #     print request.session['new_blog']
            #     request.session['blogs'].append(request.session['new_blog'])
            #     request.session['blog_holder'].append(request.session['blogs'])
            # else:
            #     del request.session['new_blog']
            #     request.session['new_blog'] = Blog(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['blogs_text'])
            #     print request.session['new_blog']
            #     request.session['blogs'].append(request.session['new_blog'])
            #     request.session['blog_holder'].append(request.session['blogs'])

            return redirect('/')
    return HttpResponse(new_rendered)

def create(request):
    return redirect('/')

def show(request):
    newest_template = loader.get_template('blogs/show.html')
    newest_rendered = newest_template.render(request=request)
    return HttpResponse(newest_rendered)