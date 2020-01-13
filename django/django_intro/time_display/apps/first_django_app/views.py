from django.shortcuts import render
# from time import gmtime, strftime
import datetime

def index(request):
    context= {
        # # "time": strftime("%Y-%m-%d %-I:%M %p", gmtime())
        # "date": strftime("%b %d, %Y", gmtime()),
        # "time": strftime("%-I:%M %p", gmtime()),
        "date": datetime.datetime.now().strftime("%b %d, %Y"),
        "time": datetime.datetime.now().strftime("%-I:%M %p"),
############# Ninja Bonus
    }
    print(context['time'])
    return render(request, 'first_django_app/index.html', context)