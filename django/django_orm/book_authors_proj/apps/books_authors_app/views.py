from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    context = {
        'all_books': Book.objects.all(),
        'all_authors': Author.objects.all(),
    }

    return render(request, 'books_authors_app/index.html', context)

def add_books(request):
    if request.method == 'POST':
        count= 0
        print(request.POST, count)
        if len(request.POST['book_input']) <= 0:
            count+=1 
        if len(request.POST['description']) <= 0:
            count+=1

        if count == 0:
            Book.objects.create(title=f"{request.POST['book_input']}", desc=f"{request.POST['description']}")
    return redirect('/')

def view_book(request, bookin_id):
    viewing = Book.objects.get(id=bookin_id)
    book_authors= Author.objects.filter(books=viewing)
    book_authors4= Author.objects.exclude(books=viewing)

    context = {
        'one_view': viewing,
        'one_book_author': book_authors,
        'one_author_book3': book_authors4,
    }
    return render(request, 'books_authors_app/index_add.html', context)

def view_book_add(request, bookin_id):
    auth= Author.objects.get(id=request.POST['option1'])
    new_b= Book.objects.get(id=bookin_id)
    new_b.authors.add(auth)
    return redirect(f'/books/{bookin_id}')


def index2(request):
    context = {
        'all_books2': Book.objects.all(),
        'all_authors2': Author.objects.all(),
    }
    return render(request, 'books_authors_app/index2.html', context)

def add_authors(request):
    if request.method == 'POST':
        count= 0
        print(request.POST, count)
        if len(request.POST['first_name_input']) <= 0:
            count+=1 
        if len(request.POST['last_name_input']) <= 0:
            count+=1
        if len(request.POST['notes_input']) <= 0:
            count+=1

        if count == 0:
            Author.objects.create(first_name=f"{request.POST['first_name_input']}", last_name=f"{request.POST['last_name_input']}", notes=f"{request.POST['notes_input']}")
    
    return redirect('/i')

def view_author(request, author_in_id):
    viewing2 = Author.objects.get(id=author_in_id)
    book_authors2= Book.objects.filter(authors=viewing2)
    book_authors3= Book.objects.exclude(authors=viewing2)
    context = {
        'one_view2': viewing2,
        'one_book_author2': book_authors2,
        'one_book_author3': book_authors3,
    }
    
    return render(request, 'books_authors_app/index_add2.html', context)

def view_author_add(request, author_in_id):
    auth2= Author.objects.get(id=author_in_id)
    new_b2= Book.objects.get(id=request.POST['option2'])
    auth2.books.add(new_b2)
    return redirect(f'/i/authors/{author_in_id}')



