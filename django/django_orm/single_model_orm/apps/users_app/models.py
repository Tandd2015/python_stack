from django.db import models

# Create your models here.
class Users(models.Model): 
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255) 
    email_address = models.CharField(max_length=255) 
    age = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __repr__(self):
    #     # fields removed for brevity
    #     return f'<Movie object: {self.title} ({self.id})>'

class OneAuthor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OneBook(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(OneAuthor, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ManyBook(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

class ManyPublisher(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(ManyBook, related_name="publishers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
