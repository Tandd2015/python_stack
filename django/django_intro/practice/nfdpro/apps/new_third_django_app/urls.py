from django.conf.urls import url
from . import views                 # the . indicates that the views file can be found in the same directory as this file
urlpatterns = [
    url(r'^index$', views.index), 
]