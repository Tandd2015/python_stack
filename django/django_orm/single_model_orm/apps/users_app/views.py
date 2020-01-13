from django.shortcuts import render
# other imports
from .models import Movie

# Create your views here.
def index(request):
    one_user= Movie.objects.create(title="Great Movie", description="The best movie ever ever ever!!!", release_date="2019-10-15", duration=123)
    context = {
        'all_the_movies': Movie.objects.all(),
        'authors': Author.objects.all(),
    }
    return render(request, 'users_app/index.html', context)


######EXAMPLE OF A NULLABLE PARAMETER
# age = models.IntegerField(default=200)	# if no age is entered for a new/existing, age will be set to 200
# age = models.IntegerField(null=True)	# if no age is provided, the field will remain empty

######CREATING
# this_author = Author.objects.get(id=2)	# get an instance of an Author
# my_book = Book.objects.create(title="Little Women", author=this_author)	# set the retrieved author as the author of a new book
    
# # or in one line...
# my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))

######READING
# some_book = Book.objects.get(id=5)

# some_book.title		# returns a string that is the title of the book
# some_book.author	# returns the Author instance associated with this book

# some_book.author.name		# return the name of the author of this book
# some_book.author.id		# returns the id of the author of this book

# this_author = Author.objects.get(id=2)
# books = Book.objects.filter(author=this_author)
    
# # one-line version:
# books = Book.objects.filter(author=Author.objects.get(id=2))

# ###### Adding a relationship between two existing records
# this_book = Book.objects.get(id=4)	# retrieve an instance of a book
# this_publisher = Publisher.objects.get(id=2)	# retrieve an instance of a publisher
    
# # 2 options that do the same thing:
# this_publisher.books.add(this_book)		# add the book to this publisher's list of books
# # OR
# this_book.publishers.add(this_publisher)	# add the publisher to this book's list of publishers

# ###### remove a relationship between two existing records
# this_book = Book.objects.get(id=4)	# retrieve an instance of a book
# this_publisher = Publisher.objects.get(id=2)	# retrieve an instance of a publisher
    
# # 2 options that do the same thing:
# this_publisher.books.remove(this_book)		# remove the book from this publisher's list of books
# # OR
# this_book.publishers.remove(this_publisher)	# remove the publisher from this book's list of publishers

# ###### syntax to see all books from a given publisher is the same as when doing a reverse look-up on a ForeignKey relationship
# this_publisher.books.all()	# get all the books this publisher is publishing
# this_book.publishers.all()	# get all the publishers for this book

# this_publisher.books.all().values()# to print	# get all the books this publisher is publishing
# this_book.publishers.all().values()# to print	# get all the publishers for this book