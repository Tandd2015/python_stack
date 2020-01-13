from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'first_video_app/index.html')

def process(request):
    print(request.POST)
    print(request.POST['name'])
    return redirect('/first_video_app/index')