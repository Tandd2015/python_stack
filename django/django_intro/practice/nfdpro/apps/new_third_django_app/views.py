from django.shortcuts import render

def index(request):
    context = {
        'name': 'Noelle',
        'favorite_color': 'turquoise',
        'pets': ['Bruce','Fitz','Georgie']
    }
    return render(request, 'new_third_django_app/index.html', context)
